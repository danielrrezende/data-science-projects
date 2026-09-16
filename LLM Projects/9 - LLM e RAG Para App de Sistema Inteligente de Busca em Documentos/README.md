# Sistema Inteligente de Busca em Documentos com IA Generativa e RAG

Um sistema completo de Retrieval-Augmented Generation (RAG) construído de ponta a ponta. Este projeto apresenta a indexação de documentos em múltiplos formatos, armazenamento de longo prazo em banco de dados vetorial, uma API backend com FastAPI conectada aos modelos LLaMA 3 hospedados pela NVIDIA (NIM), e um frontend interativo em Streamlit que exibe as respostas citando fontes exatas e permitindo downloads.

---

## 📌 Visão Geral do Projeto

Esta aplicação oferece uma arquitetura robusta de Busca de Informação Corporativa (Enterprise Q&A):
- **Ingestão Multi-formato (`ds_rag.py`):** Processamento recursivo em diretórios lendo formatos como `.pdf`, `.docx`, `.pptx` e `.txt`[cite: 31].
- **Fatiamento e Incorporações Densas (Embeddings):** Os documentos são fatiados em pedaços de 500 tokens com 50 tokens de sobreposição (`TokenTextSplitter`) e mapeados vetorialmente usando o modelo otimizado `sentence-transformers/msmarco-bert-base-dot-v5`[cite: 29, 31].
- **Banco de Dados Vetorial Qdrant:** Utiliza contêiner Docker do [Qdrant](https://qdrant.tech/) para criar índices de alta performance (`DSAVectorDB`), combinando vetores e metadados de localização de arquivos (source paths)[cite: 29, 31].
- **Backend FastAPI (`dsa_api_2.py` / `ds_start_api.py`):** Recebe consultas via rota POST, recupera os 10 chunks mais similares, constrói um contexto consolidado e solicita resposta à LLM `meta/llama3-70b-instruct` através da API da NVIDIA, exigindo estritamente o uso de citações em colchetes (ex: `[0]`)[cite: 29, 32].
- **Frontend Streamlit Web App (`ds_web_app.py`):** Um portal de conversação moderno. Lê e trata o retorno JSON da API, utiliza expressões regulares (Regex) para destacar identificadores dos documentos, apresenta o parágrafo original de contexto através de *expanders* na UI, e habilita botões para download dos anexos referenciados[cite: 28].

---

## 🛠️ Stack Tecnológico e Requisitos

- **Linguagem:** Python 3.10+
- **Banco Vetorial:** `qdrant-client` & Imagem Docker do Qdrant[cite: 23, 29]
- **Web App / UI:** `streamlit`[cite: 23, 28]
- **API Backend:** `fastapi`, `uvicorn`, `pydantic`[cite: 23, 29, 32]
- **RAG & LangChain:** `langchain`, `langchain_qdrant`, `langchain_huggingface`[cite: 23, 29, 31]
- **Processamento de Documentos:** `PyPDF2`, `python-docx`, `python-pptx`[cite: 23, 31]
- **LLM Provider:** API da NVIDIA (Llama 3 70B)[cite: 29]

---

## 🚀 Instalação e Execução

### 1. Preparação do Ambiente e Dependências

Crie um ambiente virtual (recomendado) e instale o pacote de dependências[cite: 22].

```bash
python -m venv dsaenv
source dsaenv/bin/activate  # No Windows use: dsaenv\Scripts\activate
pip install -r requirements.txt

```

### 2. Ativação do Banco Vetorial Qdrant (Docker)

Rode o contêiner do banco localmente na porta `6333`:

```bash
docker run --name vectordb -dit -p 6333:6333 qdrant/qdrant

```

*(Opcional: você pode visualizar a base criada acessando a interface gráfica no navegador em [http://localhost:6333/dashboard](http://localhost:6333/dashboard))*

### 3. Ingestão e Indexação de Documentos

Crie uma pasta com seus documentos alvo (ex: `Documentos/`) na raiz do projeto e execute a rotina de preenchimento do vetor:

```bash
python ds_rag.py Documentos

```

### 4. Configurar Token da NVIDIA API

Gere uma chave através do [NVIDIA API Catalog](https://build.nvidia.com/) e preencha a variável `nvidia_key` no arquivo `ds_env_var.py`.

```python
nvidia_key = "coloque-sua-chave-aqui"

```

### 5. Iniciar a API de Backend

Suba o serviço do FastAPI. Ele responderá na porta 8000:

```bash
python ds_start_api.py

```

### 6. Executar a Interface Web

Abra um terminal adicional (mantendo o ambiente virtual ativo) e inicie a App no Streamlit:

```bash
streamlit run ds_web_app.py

```

---

## 💻 Diagrama do Fluxo de Informação

```text
[ Documentos Locais (.pdf, .docx, .txt) ]
                   │
                   ▼
[ ds_rag.py: Quebra em Chunks + HF Embeddings ]
                   │
                   ▼
[ Qdrant Vector DB (Docker :6333) ] ◄─────┐ Buscas KNN
                                          │
[ API Backend FastAPI (ds_start_api.py) ]─┘
                   │
                   ├──► Orquestra Chamada p/ NVIDIA NIM API (Llama-3-70B)
                   ▼
[ Streamlit UI (ds_web_app.py) ]
                   ├──► Coleta prompt e envia Payload
                   ├──► Exibe Resposta com Regex parse de Citações [0], [1]
                   └──► Gera botão de download direto para o anexo base

```

---

## 📚 Agradecimentos e Referências

* Indexação e persistência vetorial hospedada por [Qdrant](https://qdrant.tech/).
* Inferência LLM corporativa alimentada pela [NVIDIA API Catalog](https://build.nvidia.com/).

<br>
<br>

---

<br>
<br>

## English
<br>

# Intelligent Document Search Engine with Generative AI and RAG

A complete end-to-end Retrieval-Augmented Generation (RAG) system. This project features multi-format document indexing, long-term storage in a vector database, a FastAPI backend connected to LLaMA 3 models hosted by NVIDIA (NIM), and an interactive Streamlit frontend that displays answers with exact source citations and enables file downloads.

---

## 📌 Project Overview

This application provides a robust Enterprise Q&A Architecture:
- **Multi-Format Ingestion (`ds_rag.py`):** Recursively processes directories reading `.pdf`, `.docx`, `.pptx`, and `.txt` formats[cite: 31].
- **Chunking & Dense Embeddings:** Documents are split into 500-token chunks with a 50-token overlap (`TokenTextSplitter`) and vectorized using the highly optimized `sentence-transformers/msmarco-bert-base-dot-v5` model[cite: 29, 31].
- **Qdrant Vector Database:** Uses a [Qdrant](https://qdrant.tech/) Docker container to create high-performance indexes (`DSAVectorDB`), combining vectors and file path metadata[cite: 29, 31].
- **FastAPI Backend (`dsa_api_2.py` / `ds_start_api.py`):** Receives queries via a POST route, retrieves the top 10 most similar chunks, builds a consolidated context, and prompts the `meta/llama3-70b-instruct` LLM via the NVIDIA API, strictly demanding bracketed citations (e.g., `[0]`)[cite: 29, 32].
- **Streamlit Web App Frontend (`ds_web_app.py`):** A modern conversational portal. It reads and parses the JSON response from the API, uses Regular Expressions (Regex) to highlight document identifiers, presents the original context paragraphs through expanders in the UI, and enables direct download buttons for the referenced attachments[cite: 28].

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+
- **Vector Database:** `qdrant-client` & Qdrant Docker Image[cite: 23, 29]
- **Web App / UI:** `streamlit`[cite: 23, 28]
- **Backend API:** `fastapi`, `uvicorn`, `pydantic`[cite: 23, 29, 32]
- **RAG & LangChain:** `langchain`, `langchain_qdrant`, `langchain_huggingface`[cite: 23, 29, 31]
- **Document Processing:** `PyPDF2`, `python-docx`, `python-pptx`[cite: 23, 31]
- **LLM Provider:** NVIDIA API Catalog (Llama 3 70B)[cite: 29]

---

## 🚀 Installation & Execution

### 1. Environment Setup and Dependencies

Create a virtual environment (recommended) and install the dependency package[cite: 22].

```bash
python -m venv dsaenv
source dsaenv/bin/activate  # On Windows use: dsaenv\Scripts\activate
pip install -r requirements.txt

```

### 2. Activate Qdrant Vector Database (Docker)

Run the database container locally on port `6333`:

```bash
docker run --name vectordb -dit -p 6333:6333 qdrant/qdrant

```

*(Optional: you can view the created database by accessing the graphical interface in your browser at [http://localhost:6333/dashboard](http://localhost:6333/dashboard))*

### 3. Document Ingestion and Indexing

Create a folder with your target documents (e.g., `Documentos/`) in the project root and execute the vector population routine:

```bash
python ds_rag.py Documentos

```

### 4. Configure NVIDIA API Token

Generate a key through the [NVIDIA API Catalog](https://build.nvidia.com/) and fill in the `nvidia_key` variable in the `ds_env_var.py` file.

```python
nvidia_key = "place-your-key-here"

```

### 5. Start the Backend API

Spin up the FastAPI service. It will respond on port 8000:

```bash
python ds_start_api.py

```

### 6. Run the Web Interface

Open an additional terminal (keeping the virtual environment active) and start the Streamlit App:

```bash
streamlit run ds_web_app.py

```

---

## 💻 Information Flow Diagram

```text
[ Local Documents (.pdf, .docx, .txt) ]
                   │
                   ▼
[ ds_rag.py: Chunk Splitting + HF Embeddings ]
                   │
                   ▼
[ Qdrant Vector DB (Docker :6333) ] ◄─────┐ KNN Searches
                                          │
[ API Backend FastAPI (ds_start_api.py) ]─┘
                   │
                   ├──► Orchestrates Call to NVIDIA NIM API (Llama-3-70B)
                   ▼
[ Streamlit UI (ds_web_app.py) ]
                   ├──► Collects prompt and sends Payload
                   ├──► Displays Response with Regex parsing for Citations [0], [1]
                   └──► Generates direct download button for the source attachment

```

---

## 📚 Acknowledgments & References

* Vector indexing and persistence hosted by [Qdrant](https://qdrant.tech/).
* Enterprise LLM inference powered by [NVIDIA API Catalog](https://build.nvidia.com/).
