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

或选择其他模型：
```bash
ollama pull qwen2:7b
ollama pull llama3:8b
```

### 3. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 4. 安装依赖

```bash
pip install -r requirements.txt
```

## 使用说明

### 运行Web应用

```bash
streamlit run app.py
```

### 使用步骤

1. 在左侧面板上传文档（支持PDF、DOCX、TXT格式）
2. 点击"构建知识库"按钮处理文档
3. 在右侧问答区域输入问题并点击"提问"
4. 查看回答结果和参考来源
5. 支持多轮对话，可查看对话历史

### 命令行版本

```bash
python rag_cli.py
```

## 项目结构与文件说明

```
├── app.py                    # Streamlit Web应用主文件，提供可视化交互界面
├── rag_cli.py                # 命令行版本，支持终端模式下的问答
├── requirements.txt          # Python依赖包列表
├── README.md                 # 项目说明文档（本文件）
├── .gitignore                # Git忽略配置，排除不必要的文件
├── docs/                     # 知识库文档文件夹（内置示例文档）
│   ├── nlp_introduction.txt          # 自然语言处理(NLP)介绍
│   ├── transformer_architecture.txt  # Transformer架构详解
│   ├── bert_introduction.txt         # BERT模型介绍
│   ├── rag_technology.txt            # RAG技术说明
│   └── llm_introduction.txt          # 大型语言模型(LLM)介绍
└── src/                      # 核心模块目录
    ├── document_loader.py    # 文档加载器：支持PDF/DOCX/TXT格式解析与文本分块
    ├── simple_rag.py         # 简化版RAG引擎：基于TF-IDF的文本匹配（无需Ollama）
    └── rag_chain.py          # 完整版RAG问答链：集成Ollama大模型（需要Ollama）
```

### 文件用途详细说明

| 文件路径 | 用途说明 | 是否必需 |
|----------|----------|----------|
| `app.py` | Web应用主入口，提供Streamlit可视化界面 | ✅ 必需 |
| `rag_cli.py` | 命令行接口，支持终端问答（需要Ollama） | ⚠️ 可选 |
| `requirements.txt` | 项目依赖列表，用于安装所需Python包 | ✅ 必需 |
| `README.md` | 项目说明文档 | ✅ 必需 |
| `.gitignore` | Git版本控制忽略配置 | ✅ 必需 |
| `src/document_loader.py` | 文档加载模块，负责读取和分割文档 | ✅ 必需 |
| `src/simple_rag.py` | TF-IDF模式RAG引擎（无需Ollama即可运行） | ✅ 必需 |
| `src/rag_chain.py` | Ollama模式RAG引擎（需要Ollama大模型） | ⚠️ 可选 |
| `docs/*.txt` | 示例知识库文档，可替换为自定义文档 | ⚠️ 可选 |

## 打包为EXE可执行文件（可选）

### 前提条件

1. 确保已安装所有依赖：`pip install -r requirements.txt`
2. 安装pyinstaller：`pip install pyinstaller`

### 打包命令

```bash
pyinstaller --onefile --windowed --name RAG-QA-System app.py
```

### 打包说明

> **⚠️ 注意**：打包生成的EXE文件仅包含Python代码和依赖库，**不包含Ollama模型**。
> 
> 运行EXE文件前，用户必须：
> 1. 在目标电脑上安装Ollama
> 2. 下载所需的模型（如：`ollama pull qwen2:7b`）
> 3. 确保Ollama服务正在运行

### 打包后的文件结构

```
dist/
└── RAG-QA-System.exe        # 可执行文件
```

### 运行EXE文件

1. 双击运行 `RAG-QA-System.exe`
2. 应用会自动在浏览器中打开
3. 如果Ollama未运行或模型未下载，会自动切换到TF-IDF模式

## 关键技术点

### RAG流程

1. **文档加载**：支持PDF、DOCX、TXT等格式的文档读取
2. **文本分块**：将长文档分割为1000字符的小块，重叠200字符
3. **向量化**：使用TF-IDF或Sentence-BERT将文本转换为向量
4. **向量存储**：使用Chroma向量数据库存储和检索（Ollama模式）
5. **问答生成**：结合检索结果生成回答

### 运行模式说明

| 模式 | 所需依赖 | 特点 |
|------|----------|------|
| **TF-IDF模式** | 仅需Python依赖 | 无需Ollama，开箱即用，回答基于文本匹配 |
| **Ollama模式** | Ollama + 模型 | 需要下载模型，回答质量更高，支持复杂推理 |

### 模型配置

- **嵌入模型**：all-MiniLM-L6-v2（轻量级，适合本地部署）
- **大模型**：deepseek-r1:7b（默认），支持qwen2:7b、llama3:8b等
- **向量数据库**：Chroma（轻量级，无需额外服务）

## 测试示例

### 相关问题
1. 什么是自然语言处理？
2. Transformer架构的核心组件有哪些？
3. BERT的预训练任务是什么？
4. RAG技术的优势是什么？
5. 大型语言模型面临哪些挑战？

### 无关问题（应返回"文档中未找到相关答案"）
1. 今天天气怎么样？
2. 中国的首都是哪里？

## 注意事项

1. 首次运行需要下载嵌入模型，可能需要几分钟时间
2. 确保Ollama服务已启动（运行 `ollama serve`）
3. 建议使用GPU加速以获得更好的性能
4. 文档文件不要过大，建议单文件不超过50MB
5. 打包的EXE文件不包含Ollama模型，需要单独安装

## 已知问题与改进方向

- [ ] 支持更多文档格式（如Markdown、Excel）
- [ ] 添加文档预览功能
- [ ] 支持批量删除文档
- [ ] 添加夜间模式
- [ ] 支持导出问答记录

## License

MIT License