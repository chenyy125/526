import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SimpleRAG:
    def __init__(self):
        self.chunks = []
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
        self.tfidf_matrix = None
    
    def add_documents(self, documents):
        self.chunks.extend(documents)
        if self.chunks:
            texts = [doc.page_content if hasattr(doc, 'page_content') else doc for doc in self.chunks]
            self.tfidf_matrix = self.vectorizer.fit_transform(texts)
    
    def search(self, query, k=3):
        if not self.chunks or self.tfidf_matrix is None:
            return []
        
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_indices = np.argsort(similarities)[::-1][:k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.01:
                chunk = self.chunks[idx]
                if hasattr(chunk, 'page_content'):
                    results.append({
                        'content': chunk.page_content,
                        'source': chunk.metadata.get('source', 'Unknown'),
                        'similarity': similarities[idx]
                    })
                else:
                    results.append({
                        'content': chunk,
                        'source': 'Unknown',
                        'similarity': similarities[idx]
                    })
        
        return results
    
    def generate_answer(self, query):
        results = self.search(query, k=5)
        
        if not results:
            return "文档中未找到相关答案", []
        
        context = "\n\n".join([r['content'] for r in results])
        
        keywords = self.extract_keywords(query)
        answer = self.synthesize_answer(query, context, keywords, results)
        
        return answer, results
    
    def extract_keywords(self, query):
        query = query.lower()
        keywords = re.findall(r'[\u4e00-\u9fa5a-zA-Z]+', query)
        return keywords[:10]
    
    def synthesize_answer(self, query, context, keywords, results):
        sentences = context.split('。')
        relevant_sentences = []
        
        for sentence in sentences:
            for keyword in keywords:
                if keyword and len(keyword) > 1 and keyword.lower() in sentence.lower():
                    relevant_sentences.append(sentence.strip())
                    break
        
        if relevant_sentences:
            answer = '。'.join([s for s in relevant_sentences[:3] if s]) + '。'
            if len(answer) > 500:
                answer = answer[:500] + '...'
            return answer
        
        if results:
            top_result = results[0]
            content = top_result['content']
            sentences = [s.strip() for s in content.split('。') if s.strip()]
            if sentences:
                answer = '。'.join(sentences[:3]) + '。'
                return answer
        
        return "文档中未找到相关答案"

def create_simple_rag_chain(chunks):
    rag = SimpleRAG()
    rag.add_documents(chunks)
    return rag

def ask_simple_question(rag, question):
    answer, sources = rag.generate_answer(question)
    return answer, sources