```python
readme_content = """# Talk to Your PDFs: Personal AI Assistant with LangChain & ChromaDB

A Retrieval-Augmented Generation (RAG) system built in Python to chat with PDF documents using OpenAI embeddings, Chroma vector store, and LangChain QA chains.

---

## 📌 Project Overview

This project implements a question-answering AI assistant over local PDF documents using a RAG architecture:
- Loads PDF files from a directory using `PyPDFDirectoryLoader`.
- Computes vector representations of document contents using `OpenAIEmbeddings`.
- Indexes document embeddings inside an in-memory vector store using `Chroma`.
- Performs similarity search (k-NN) to fetch the top-$k$ relevant passages.
- Answers user queries contextually using an OpenAI LLM via LangChain's `load_qa_chain` ("stuff" chain type).

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+ (tested on Python 3.11.5)
- **Frameworks & Libraries:**
  - `langchain` & `langchain-community`
  - `chromadb`
  - `openai`
  - `pypdf` (for PDF text extraction via `PyPDFDirectoryLoader`)
  - `python-dotenv` (for API key management)
  - `watermark` (for version tracking)

---

## 🚀 Installation & Setup

1. **Clone the repository and install dependencies:**

   ```bash
   pip install -r requirements.txt
   pip install watermark python-dotenv

```

2. **Configure OpenAI API Key:**
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here

```


3. **Add PDF Documents:**
Create a directory named `arquivos/` (or your preferred folder path) and drop your `.pdf` documents inside it.

---

## 📂 Architecture & Workflow

```
[ PDF Files in 'arquivos/' ]
           │
           ▼
[ PyPDFDirectoryLoader ] ──► Extracts Text & Metadata
           │
           ▼
[ OpenAIEmbeddings ] ──► Converts Text into Dense Vector Embeddings
           │
           ▼
[ Chroma Vector Store ] ──► Stores & Indexes Vectors ('dsa-index')
           │
           ├──► Similarity Search (k=2)
           ▼
[ LangChain QA 'Stuff' Chain ] ◄── OpenAI LLM (temperature=0.3)
           │
           ▼
[ Grounded Answer Generation ]

```

---

## 💻 Code Example / Usage

```python
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# 1. Load Environment Variables
load_dotenv()

# 2. Extract Text from PDFs
loader = PyPDFDirectoryLoader("arquivos/")
documents = loader.load()

# 3. Create Embeddings and Initialize ChromaDB
embeddings = OpenAIEmbeddings(api_key=os.environ["OPENAI_API_KEY"])
vector_store = Chroma.from_documents(
    documents,
    embeddings,
    collection_name="dsa-index"
)

# 4. Set up QA Chain
llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.3)
chain = load_qa_chain(llm, chain_type="stuff")

# 5. Query Function
def ask_pdf(query: str, k: int = 2) -> str:
    relevant_docs = vector_store.similarity_search(query, k=k)
    return chain.run(input_documents=relevant_docs, question=query)

# Example Execution
response = ask_pdf("What was found by the recent Salesforce survey?")
print(response)

```

---

## 💬 Sample Queries & Results

* **Query 1:** *"O que a pesquisa recente da Salesforce descobriu?"*
**Answer:** A pesquisa recente da Salesforce descobriu que três quartos dos trabalhadores do mundo se sentem despreparados para os empregos que podem encontrar após o marco em que o número de horas trabalhadas pelas máquinas será igual ao número de horas trabalhadas pelos humanos.
* **Query 2:** *"Qual percentual de empregadores estão tendo problemas para preencher vagas digitais com candidatos qualificados?"*
**Answer:** Quase 60% dos empregadores estão tendo problemas para preencher vagas digitais com candidatos qualificados.
* **Query 3:** *"Qual a habilidade mais importante na era da Inteligência Artificial?"*
**Answer:** "Seja Bom em Aprender".

---

## 📚 Acknowledgments & References

* Project developed as part of coursework at [Data Science Academy](https://www.datascienceacademy.com.br).
* Vector store powered by [ChromaDB](https://www.trychroma.com/).
* Orchestration powered by [LangChain](https://python.langchain.com/).
"""

with open("README_RAG.md", "w", encoding="utf-8") as f:
f.write(readme_content)

print("README_RAG.md created successfully!")

```

```text?code_stdout&code_event_index=1
README_RAG.md created successfully!


```

An English `README.md` based on your RAG notebook:

```markdown
# Talk to Your PDFs: Personal AI Assistant with LangChain & ChromaDB

A Retrieval-Augmented Generation (RAG) system built in Python to chat with PDF documents using OpenAI embeddings, Chroma vector store, and LangChain QA chains.

---

## 📌 Project Overview

This project implements a question-answering AI assistant over local PDF documents using a RAG architecture:
- Loads PDF files from a directory using `PyPDFDirectoryLoader`.
- Computes vector representations of document contents using `OpenAIEmbeddings`.
- Indexes document embeddings inside an in-memory vector store using `Chroma`.
- Performs similarity search (k-NN) to fetch the top-$k$ relevant passages.
- Answers user queries contextually using an OpenAI LLM via LangChain's `load_qa_chain` ("stuff" chain type).

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+ (tested on Python 3.11.5)
- **Frameworks & Libraries:**
  - `langchain` & `langchain-community`
  - `chromadb`
  - `openai`
  - `pypdf` (for PDF text extraction via `PyPDFDirectoryLoader`)
  - `python-dotenv` (for API key management)
  - `watermark` (for version tracking)

---

## 🚀 Installation & Setup

1. **Clone the repository and install dependencies:**

   ```bash
   pip install -r requirements.txt
   pip install watermark python-dotenv

```

2. **Configure OpenAI API Key:**
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here

```


3. **Add PDF Documents:**
Create a directory named `arquivos/` (or adjust the folder path in the code) and drop your `.pdf` documents inside it.

---

## 📂 Architecture & Workflow

```
[ PDF Files in 'arquivos/' ]
           │
           ▼
[ PyPDFDirectoryLoader ] ──► Extracts Text & Metadata
           │
           ▼
[ OpenAIEmbeddings ] ──► Converts Text into Dense Vector Embeddings
           │
           ▼
[ Chroma Vector Store ] ──► Stores & Indexes Vectors ('dsa-index')
           │
           ├──► Similarity Search (k=2)
           ▼
[ LangChain QA 'Stuff' Chain ] ◄── OpenAI LLM (temperature=0.3)
           │
           ▼
[ Grounded Answer Generation ]

```

---

## 💻 Code Example / Usage

```python
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# 1. Load Environment Variables
load_dotenv()

# 2. Extract Text from PDFs
loader = PyPDFDirectoryLoader("arquivos/")
documents = loader.load()

# 3. Create Embeddings and Initialize ChromaDB
embeddings = OpenAIEmbeddings(api_key=os.environ["OPENAI_API_KEY"])
vector_store = Chroma.from_documents(
    documents,
    embeddings,
    collection_name="dsa-index"
)

# 4. Set up QA Chain
llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.3)
chain = load_qa_chain(llm, chain_type="stuff")

# 5. Query Function
def ask_pdf(query: str, k: int = 2) -> str:
    relevant_docs = vector_store.similarity_search(query, k=k)
    return chain.run(input_documents=relevant_docs, question=query)

# Example Execution
response = ask_pdf("O que a pesquisa recente da Salesforce descobriu?")
print(response)

```

---

## 💬 Sample Queries & Results

* **Query 1:** *"O que a pesquisa recente da Salesforce descobriu?"*
**Answer:** A pesquisa recente da Salesforce descobriu que três quartos dos trabalhadores do mundo se sentem despreparados para os empregos que podem encontrar após o marco em que o número de horas trabalhadas pelas máquinas será igual ao número de horas trabalhadas pelos humanos.


* **Query 2:** *"Qual percentual de empregadores estão tendo problemas para preencher vagas digitais com candidatos qualificados?"*
**Answer:** Quase 60% dos empregadores estão tendo problemas para preencher vagas digitais com candidatos qualificados.


* **Query 3:** *"Qual a habilidade mais importante na era da Inteligência Artificial?"*
**Answer:** "Seja Bom em Aprender".



---

## 📚 Acknowledgments & References

* Project developed as part of coursework at [Data Science Academy](https://www.datascienceacademy.com.br).


* Vector store powered by [ChromaDB](https://www.trychroma.com/).


* Orchestration powered by [LangChain](https://python.langchain.com/).



```

```
