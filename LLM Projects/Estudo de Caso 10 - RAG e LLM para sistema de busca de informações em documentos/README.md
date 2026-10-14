<a id="top"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

---

<a id="pt-br"></a>

# 🇧🇷 Assistente IA - Sistema RAG com OCR e Indexação Paralela

Sistema completo de **RAG (Retrieval-Augmented Generation)** projetado para consulta e análise de documentos e autos judiciais. O projeto combina extração inteligente de texto (com fallback automático para OCR em documentos escaneados), indexação incremental paralelizada, banco de dados vetorial **Qdrant**, API em **FastAPI** com templates **Jinja2** e interface web interativa em **Streamlit** com mapeamento automático de citações para os arquivos originais.

---

## 🚀 Principais Funcionalidades

* **Indexação Incremental Inteligente:** Controle via hash MD5 (`arquivos_indexados.json`) que processa apenas arquivos novos ou modificados, evitando retrabalho.
* **Processamento Paralelo:** Extração de texto e *chunking* distribuídos em múltiplos núcleos da CPU (`ProcessPoolExecutor`).
* **OCR Automático:** Detecção automática de PDFs escaneados (quando a extração nativa retorna menos de 50 caracteres) e leitura direta de imagens utilizando `Tesseract OCR`.
* **Prompts Dinâmicos com Jinja2:** Flexibilidade para customizar instruções de sistema na pasta `prompts/`.
* **Rastreabilidade e Hiperlinks Automáticos:** O sistema identifica o ID numérico dos documentos (ex.: `ID72495028`) e transforma as citações na resposta da IA em links clicáveis que abrem o documento original diretamente no navegador.

---

## 📂 Arquitetura e Estrutura do Projeto

```text
├── Documentos/               # Diretório onde ficam os arquivos a serem indexados
├── prompts/                  # Diretório contendo os templates Jinja2 (ex: prompt_contexto.j2)
├── rag.py                    # Pipeline de ingestão, OCR, chunking e vetorização no Qdrant
├── rag_api.py                # Backend FastAPI, integração LangChain + Qdrant + NVIDIA NIM
├── rag_start_api.py          # Script de inicialização do servidor Uvicorn (porta 9000, 4 workers)
├── rag_web_app.py            # Interface web em Streamlit com resolução de links dos documentos
├── rag_env_var.py            # Configuração da chave de API da NVIDIA
├── arquivos_indexados.json   # Gerado automaticamente para controle de hashes MD5
├── requirements.txt          # Dependências Python do projeto
└── LEIAME.txt                # Instruções rápidas de linha de comando
```

---

## 📄 Tipos de Documentos Suportados

O módulo de vetorização (`rag.py`) varre pastas recursivamente e suporta **10 formatos de arquivo**:

| Categoria | Extensões | Biblioteca / Método | Comportamento Especial |
| :--- | :--- | :--- | :--- |
| **Documentos PDF** | `.pdf` | `PyPDF2`, `pdf2image`, `pytesseract` | Tenta extração nativa primeiro. Se retornar `< 50` caracteres, converte as páginas em imagens (200 DPI) e aplica OCR (`por+eng`). |
| **Texto Puro** | `.txt` | `open()` nativo | Leitura em `utf-8` ignorando erros de codificação (`errors="ignore"`). |
| **Microsoft Word** | `.docx` | `python-docx` | Extrai o texto de todos os parágrafos (`doc.paragraphs`). |
| **PowerPoint** | `.pptx` | `python-pptx` | Extrai o texto de todos os *shapes* em cada slide da apresentação. |
| **Imagens** | `.jpg`, `.jpeg`, `.png`, `.tiff`, `.tif`, `.bmp` | `Pillow (PIL)`, `pytesseract` | Aplica OCR diretamente sobre a imagem (`por+eng`). |

---

## 🛠️ Pré-requisitos de Sistema

Além do **Python 3.10+** e do **Docker**, o funcionamento do OCR e da conversão de PDFs exige pacotes nativos instalados no sistema operacional:

### Ubuntu / Debian
```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-por tesseract-ocr-eng poppler-utils
```

### macOS (via Homebrew)
```bash
brew install tesseract tesseract-lang poppler
```

---

## ⚙️ Instalação e Configuração

### 1. Criar e ativar o ambiente virtual
```bash
python -m venv ragenv
source ragenv/bin/activate  # No Windows: ragenv\Scripts\activate
```

### 2. Instalar as dependências Python
```bash
pip install -r requirements.txt
```

### 3. Configurar a Chave de API (NVIDIA NIM)
Edite o arquivo `rag_env_var.py` e insira a sua chave da API da NVIDIA:
```python
nvidia_key = "nvapi-sua-chave-aqui"
```
*(Alternativamente, defina a variável de ambiente `NVIDIA_API_KEY` no seu sistema).*

### 4. Configurar os Templates de Prompt
Certifique-se de que a pasta `prompts/` contenha o arquivo `prompt_contexto.j2` (template padrão requisitado pela API).

---

## ▶️ Como Executar o Projeto

### Passo 1: Iniciar o Banco Vetorial (Qdrant) via Docker
Crie e inicie o container do Qdrant na porta `6333`:
```bash
docker run --name vectordb -dit -p 6333:6333 qdrant/qdrant
```
> **Dica:** Caso o container já exista, basta iniciá-lo com `docker start vectordb`.  
> O painel web do Qdrant pode ser acessado em: [http://localhost:6333/dashboard](http://localhost:6333/dashboard)

### Passo 2: Indexar e Vetorizar os Documentos
Coloque seus arquivos na pasta `Documentos` (ou indique outro diretório) e execute o indexador:
```bash
python rag.py Documentos
```

> **Reindexação completa (Reset):** Caso mude o modelo de embedding ou queira recriar o banco do zero:
> ```bash
> curl -X DELETE http://localhost:6333/collections/ragVectorDB
> rm -f arquivos_indexados.json
> python rag.py Documentos
> ```

### Passo 3: Iniciar a API (Backend)
Em um terminal (com o ambiente `ragenv` ativo), inicie o servidor FastAPI:
```bash
python rag_start_api.py
```
A API ficará disponível em `http://localhost:9000` (Documentação Swagger em `http://localhost:9000/docs`).

### Passo 4: Iniciar a Aplicação Web (Frontend)
Em um **novo terminal** (também com o ambiente `ragenv` ativo), execute o Streamlit:
```bash
streamlit run rag_web_app.py
```

---

## 🔧 Parâmetros Técnicos e Customização

Os principais hiperparâmetros podem ser ajustados diretamente no topo dos arquivos `rag.py` e `rag_api.py`:

* **Modelo de Embedding:** `sentence-transformers/all-MiniLM-L6-v2` (384 dimensões, distância Cosseno).
* **Chunking:** `CHUNK_SIZE = 800` tokens | `CHUNK_OVERLAP = 80` tokens (`TokenTextSplitter`).
* **LLM (NVIDIA NIM):** `openai/gpt-oss-20b` (`temperature = 0.2`, `max_tokens = 4096`).
* **Recuperação (Retriever):** `K_RESULTADOS = 8` trechos mais relevantes por consulta.
* **OCR:** Idioma `por+eng` com resolução de `200 DPI`.

---

## 🔌 Endpoints da API (`rag_api.py`)

* `GET /` — Verifica o status da API, modelos carregados e configurações ativas.
* `GET /prompts` — Lista os templates `.j2` disponíveis no diretório `prompts/`.
* `POST /rag_api` — Recebe `{"query": "sua pergunta", "template": "prompt_contexto.j2"}` e retorna a resposta gerada (`answer`) junto aos trechos recuperados (`context`).
* `GET /arquivos/{caminho_do_arquivo}` — Endpoint estático que serve os documentos originais para abertura direta via navegador.

<br>

[⬆️ Voltar ao topo](#top) | [🇺🇸 Read in English](#en)

<br>

---

<br>

<a id="en"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

# 🇺🇸 AI Assistant - RAG System with OCR and Parallel Indexing

A complete **RAG (Retrieval-Augmented Generation)** system designed for querying and analyzing legal documents and court records. The project combines intelligent text extraction (with automatic OCR fallback for scanned documents), parallelized incremental indexing, a **Qdrant** vector database, a **FastAPI** backend with **Jinja2** templates, and an interactive **Streamlit** web interface with automatic citation mapping to the original files.

---

## 🚀 Key Features

* **Intelligent Incremental Indexing:** MD5 hash tracking (`arquivos_indexados.json`) that processes only new or modified files, avoiding redundant work.
* **Parallel Processing:** Text extraction and chunking distributed across multiple CPU cores (`ProcessPoolExecutor`).
* **Automatic OCR:** Automatic detection of scanned PDFs (when native extraction returns fewer than 50 characters) and direct image reading using `Tesseract OCR`.
* **Dynamic Prompts with Jinja2:** Flexibility to customize system instructions inside the `prompts/` folder.
* **Traceability and Automatic Hyperlinks:** The system identifies the numeric ID of the documents (e.g., `ID72495028`) and turns citations in the AI's response into clickable links that open the original document directly in the browser.

---

## 📂 Architecture and Project Structure

```text
├── Documentos/               # Directory where files to be indexed are stored
├── prompts/                  # Directory containing Jinja2 templates (e.g., prompt_contexto.j2)
├── rag.py                    # Ingestion pipeline, OCR, chunking, and vectorization in Qdrant
├── rag_api.py                # FastAPI backend, LangChain + Qdrant + NVIDIA NIM integration
├── rag_start_api.py          # Uvicorn server startup script (port 9000, 4 workers)
├── rag_web_app.py            # Streamlit web interface with document link resolution
├── rag_env_var.py            # NVIDIA API key configuration
├── arquivos_indexados.json   # Automatically generated for MD5 hash tracking
├── requirements.txt          # Project Python dependencies
└── LEIAME.txt                # Quick command-line instructions
```

---

## 📄 Supported Document Types

The vectorization module (`rag.py`) recursively scans folders and supports **10 file formats**:

| Category | Extensions | Library / Method | Special Behavior | 
| :--- | :--- | :--- | :--- | 
| **PDF Documents** | `.pdf` | `PyPDF2`, `pdf2image`, `pytesseract` | Attempts native extraction first. If it returns `< 50` characters, converts pages to images (200 DPI) and applies OCR (`por+eng`). | 
| **Plain Text** | `.txt` | Native `open()` | Reads in `utf-8` ignoring encoding errors (`errors="ignore"`). | 
| **Microsoft Word** | `.docx` | `python-docx` | Extracts text from all paragraphs (`doc.paragraphs`). | 
| **PowerPoint** | `.pptx` | `python-pptx` | Extracts text from all shapes in each slide of the presentation. | 
| **Images** | `.jpg`, `.jpeg`, `.png`, `.tiff`, `.tif`, `.bmp` | `Pillow (PIL)`, `pytesseract` | Applies OCR directly on the image (`por+eng`). | 

---

## 🛠️ System Prerequisites

In addition to **Python 3.10+** and **Docker**, OCR functionality and PDF conversion require native packages installed on the operating system:

### Ubuntu / Debian
```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-por tesseract-ocr-eng poppler-utils
```

### macOS (via Homebrew)
```bash
brew install tesseract tesseract-lang poppler
```

---

## ⚙️ Installation and Configuration

### 1. Create and activate the virtual environment
```bash
python -m venv ragenv
source ragenv/bin/activate  # On Windows: ragenv\Scripts\activate
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure the API Key (NVIDIA NIM)
Edit the `rag_env_var.py` file and insert your NVIDIA API key:
```python
nvidia_key = "nvapi-your-key-here"
```
*(Alternatively, set the `NVIDIA_API_KEY` environment variable in your system).*

### 4. Configure Prompt Templates
Make sure the `prompts/` folder contains the `prompt_contexto.j2` file (the default template requested by the API).

---

## ▶️ How to Run the Project

### Step 1: Start the Vector Database (Qdrant) via Docker
Create and start the Qdrant container on port `6333`:
```bash
docker run --name vectordb -dit -p 6333:6333 qdrant/qdrant
```
> **Tip:** If the container already exists, simply start it with `docker start vectordb`.  
> The Qdrant web dashboard can be accessed at: [http://localhost:6333/dashboard](http://localhost:6333/dashboard)

### Step 2: Index and Vectorize the Documents
Place your files in the `Documentos` folder (or specify another directory) and run the indexer:
```bash
python rag.py Documentos
```

> **Full Re-indexing (Reset):** If you change the embedding model or want to recreate the database from scratch:
> ```bash
> curl -X DELETE http://localhost:6333/collections/ragVectorDB
> rm -f arquivos_indexados.json
> python rag.py Documentos
> ```

### Step 3: Start the API (Backend)
In a terminal (with the `ragenv` environment active), start the FastAPI server:
```bash
python rag_start_api.py
```
The API will be available at `http://localhost:9000` (Swagger documentation at `http://localhost:9000/docs`).

### Step 4: Start the Web Application (Frontend)
In a **new terminal** (also with the `ragenv` environment active), run Streamlit:
```bash
streamlit run rag_web_app.py
```

---

## 🔧 Technical Parameters and Customization

The main hyperparameters can be adjusted directly at the top of the `rag.py` and `rag_api.py` files:

* **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions, Cosine distance).
* **Chunking:** `CHUNK_SIZE = 800` tokens | `CHUNK_OVERLAP = 80` tokens (`TokenTextSplitter`).
* **LLM (NVIDIA NIM):** `openai/gpt-oss-20b` (`temperature = 0.2`, `max_tokens = 4096`).
* **Retrieval (Retriever):** `K_RESULTADOS = 8` most relevant chunks per query.
* **OCR:** Language `por+eng` at `200 DPI` resolution.

---

## 🔌 API Endpoints (`rag_api.py`)

* `GET /` — Checks the API status, loaded models, and active configurations.
* `GET /prompts` — Lists the available `.j2` templates in the `prompts/` directory.
* `POST /rag_api` — Receives `{"query": "your question", "template": "prompt_contexto.j2"}` and returns the generated response (`answer`) along with the retrieved chunks (`context`).
* `GET /arquivos/{file_path}` — Static endpoint that serves the original documents for direct opening in the browser.

<br>

[⬆️ Back to top](#top) | [🇧🇷 Ler em Português](#pt-br)
