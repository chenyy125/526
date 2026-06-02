# RAG智能问答系统

基于本地知识库的RAG智能问答系统，支持PDF、DOCX、TXT等多种文档格式，使用Ollama本地大模型进行问答。

**项目地址**: https://github.com/chenyy125/526

## 功能特点

- 📁 支持多种文档格式（PDF、DOCX、TXT）
- 🔍 基于向量数据库的文档检索
- 💬 支持多轮对话，具有会话记忆功能
- 📊 实时显示知识库状态
- 🚀 支持多种Ollama模型切换

## 环境要求

- Python 3.10+
- Ollama（用于部署本地大模型）
- 至少8GB内存（推荐16GB+）

## 安装步骤

### 1. 安装Ollama

访问 [Ollama官方网站](https://ollama.com/) 下载并安装Ollama。

### 2. 下载模型

```bash
ollama pull deepseek-r1:7b
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

## 使用说明

```bash
streamlit run app.py
```

## License

MIT License