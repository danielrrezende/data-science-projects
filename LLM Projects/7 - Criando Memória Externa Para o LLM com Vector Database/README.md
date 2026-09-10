# External Vector Memory for LLMs with FAISS and LLaMA 3

A Retrieval-Augmented Generation (RAG) system implementing external long-term vector memory using **Unstructured API**, **BAAI/bge-m3 embeddings**, **FAISS**, and a quantized 4-bit **Meta-Llama-3-8B-Instruct** model orchestrated via **LangChain**.

---

## 📌 Project Overview

This project builds an end-to-end question-answering architecture using local PDF files as external knowledge:
- **Document Partitioning & Ingestion:** Connects to the `unstructured-client` API to extract and partition text from raw PDF documents (`ArtigoDSA1.pdf`) into chunks by title (`by_title`, max 512 characters).
- **Dense Multilingual Embeddings:** Vectorizes document elements into semantic vectors using the high-performing multilingual model `BAAI/bge-m3`.
- **Vector Store Indexing:** Indexes chunk representations using a GPU-accelerated **FAISS** vector store and configures a top-$k$ similarity retriever ($k=4$).
- **Quantized LLaMA 3 Inference:** Loads `meta-llama/Meta-Llama-3-8B-Instruct` in 4-bit precision (`BitsAndBytesConfig`, `nf4`, `bfloat16`) with custom token terminators (`<|eot_id|>`).
- **RAG Chain Composition:** Assembles an LCEL (LangChain Expression Language) pipeline (`retriever | prompt | llm | StrOutputParser`) instructing the model to answer colloquially in Brazilian Portuguese based strictly on retrieved context.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+ (tested on Python 3.11.5)
- **Hardware Requirement:** GPU with CUDA support (e.g., NVIDIA A100 40GB)
- **Frameworks & Key Libraries:**
  - `langchain` & `langchain-community`
  - `transformers`, `accelerate`, `bitsandbytes`
  - `sentence-transformers`
  - `faiss-gpu`
  - `unstructured` & `unstructured-client`
  - `watermark`

---

## 🚀 Installation & Setup

1. **Install dependencies:**
   ```bash
   pip install -q unstructured_client unstructured
   pip install -q langchain langchain-community transformers accelerate bitsandbytes sentence-transformers faiss-gpu watermark

```

2. **Set Environment Variables & Tokens:**
* Set your Unstructured API key:
```python
os.environ["UNSTRUCTURED_API_KEY"] = "your_unstructured_api_key"

```


* Authenticate with Hugging Face (required to download Meta LLaMA 3 weights):
```python
from huggingface_hub.hf_api import HfFolder
HfFolder.save_token("your_huggingface_token")

```




3. **Prepare Knowledge Documents:**
Place target PDF files in the `arquivos/` directory (e.g., `arquivos/ArtigoDSA1.pdf`).

---

## ⚙️ Architecture & Pipeline Flow

```
[ PDF Document: arquivos/ArtigoDSA1.pdf ]
                     │
                     ▼
[ Unstructured API Partitioning (by_title, 512 chars) ]
                     │
                     ▼
[ BAAI/bge-m3 Embeddings ] ──► Dense Vectors
                     │
                     ▼
[ FAISS Vector Store Index ] ──► Similarity Retriever (k=4)
                     │
                     ▼
[ LLaMA 3 Prompt Template (<|start_header_id|>...) ]
                     │
                     ▼
[ Meta-Llama-3-8B-Instruct (4-bit NF4) ]
                     │
                     ▼
[ Grounded Conversational Answer in PT-BR ]

```

---

## 💻 Code Example & Usage

```python
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. Define LLaMA 3 Chat Prompt Template
prompt_template = \"\"\"
<|start_header_id|>user<|end_header_id|>
Você é um assistente para tirar dúvidas sobre Inteligência Artificial.
Você recebe as partes extraídas de um documento longo e uma pergunta. Forneça uma resposta coloquial.
Se você não souber a resposta, basta dizer “Não sei”. Não invente uma resposta. Responda em português do Brasil.
Pergunta: {question}
Contexto: {context}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
\"\"\"

# 2. Build LCEL Chain
llm_chain = prompt | llm | StrOutputParser()
rag_chain = {"context": retriever, "question": RunnablePassthrough()} | llm_chain

# 3. Query the Knowledge Base
answer = rag_chain.invoke("O que a pandemia do Covid-19 gerou no desenvolvimento digital?")
print(answer)

```

---

## 💬 Sample Queries & Responses

* **Query 1:** *"O que a pandemia do Covid-19 gerou no desenvolvimento digital?"*
**Generated Answer:** A pandemia do Covid-19 gerou um impulso significativo no desenvolvimento digital, acelerando a transição de reuniões, consultas médicas e interações cotidianas para o ambiente online, além de evidenciar a escassez de profissionais qualificados em competências digitais.
* **Query 2:** *"Quanto as principais economias do mundo podem perder até 2028 em crescimento potencial?"*
**Generated Answer:** Com base no contexto fornecido pela Accenture, a estimativa é de que a lacuna de habilidades possa gerar uma perda potencial de até US$ 11,5 trilhões em crescimento econômico global até 2028.

---

## 📚 Acknowledgments & References

* Project developed as part of coursework at [Data Science Academy](https://www.datascienceacademy.com.br).
* Document ingestion powered by [Unstructured.io](https://unstructured.io/).
* Embeddings powered by [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3).
* Base LLM provided by [Meta via Hugging Face (`meta-llama/Meta-Llama-3-8B-Instruct`)](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct).
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content_p7)

print("README.md for Projeto 7 created successfully!")

```

```text?code_stdout&code_event_index=1
README.md for Projeto 7 created successfully!


```

O arquivo **`README.md`** para o notebook do Projeto 7 (Memória Externa para LLMs com FAISS, Unstructured, BGE-M3 e LLaMA 3) foi gerado e está disponível para download:

📥 **[Baixar README.md](https://www.google.com/search?q=sandbox:/README.md)**

---

### Conteúdo completo do arquivo:

```markdown
# External Vector Memory for LLMs with FAISS and LLaMA 3

A Retrieval-Augmented Generation (RAG) system implementing external long-term vector memory using **Unstructured API**, **BAAI/bge-m3 embeddings**, **FAISS**, and a quantized 4-bit **Meta-Llama-3-8B-Instruct** model orchestrated via **LangChain**.

---

## 📌 Project Overview

This project builds an end-to-end question-answering architecture using local PDF files as external knowledge:
- **Document Partitioning & Ingestion:** Connects to the `unstructured-client` API to extract and partition text from raw PDF documents (`ArtigoDSA1.pdf`) into chunks by title (`by_title`, max 512 characters).
- **Dense Multilingual Embeddings:** Vectorizes document elements into semantic vectors using the high-performing multilingual model `BAAI/bge-m3`.
- **Vector Store Indexing:** Indexes chunk representations using a GPU-accelerated **FAISS** vector store and configures a top-$k$ similarity retriever ($k=4$).
- **Quantized LLaMA 3 Inference:** Loads `meta-llama/Meta-Llama-3-8B-Instruct` in 4-bit precision (`BitsAndBytesConfig`, `nf4`, `bfloat16`) with custom token terminators (`<|eot_id|>`).
- **RAG Chain Composition:** Assembles an LCEL (LangChain Expression Language) pipeline (`retriever | prompt | llm | StrOutputParser`) instructing the model to answer colloquially in Brazilian Portuguese based strictly on retrieved context.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+ (tested on Python 3.11.5)
- **Hardware Requirement:** GPU with CUDA support (e.g., NVIDIA A100 40GB)
- **Frameworks & Key Libraries:**
  - `langchain` & `langchain-community`
  - `transformers`, `accelerate`, `bitsandbytes`
  - `sentence-transformers`
  - `faiss-gpu`
  - `unstructured` & `unstructured-client`
  - `watermark`

---

## 🚀 Installation & Setup

1. **Install dependencies:**
   ```bash
   pip install -q unstructured_client unstructured
   pip install -q langchain langchain-community transformers accelerate bitsandbytes sentence-transformers faiss-gpu watermark

```

2. **Set Environment Variables & Tokens:**
* Set your Unstructured API key:
```python
os.environ["UNSTRUCTURED_API_KEY"] = "your_unstructured_api_key"

```


* Authenticate with Hugging Face (required to download Meta LLaMA 3 weights):
```python
from huggingface_hub.hf_api import HfFolder
HfFolder.save_token("your_huggingface_token")

```




3. **Prepare Knowledge Documents:**
Place target PDF files in the `arquivos/` directory (e.g., `arquivos/ArtigoDSA1.pdf`).

---

## ⚙️ Architecture & Pipeline Flow

```
[ PDF Document: arquivos/ArtigoDSA1.pdf ]
                     │
                     ▼
[ Unstructured API Partitioning (by_title, 512 chars) ]
                     │
                     ▼
[ BAAI/bge-m3 Embeddings ] ──► Dense Vectors
                     │
                     ▼
[ FAISS Vector Store Index ] ──► Similarity Retriever (k=4)
                     │
                     ▼
[ LLaMA 3 Prompt Template (<|start_header_id|>...) ]
                     │
                     ▼
[ Meta-Llama-3-8B-Instruct (4-bit NF4) ]
                     │
                     ▼
[ Grounded Conversational Answer in PT-BR ]

```

---

## 💻 Code Example & Usage

```python
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. Define LLaMA 3 Chat Prompt Template
prompt_template = """
<|start_header_id|>user<|end_header_id|>
Você é um assistente para tirar dúvidas sobre Inteligência Artificial.
Você recebe as partes extraídas de um documento longo e uma pergunta. Forneça uma resposta coloquial.
Se você não souber a resposta, basta dizer “Não sei”. Não invente uma resposta. Responda em português do Brasil.
Pergunta: {question}
Contexto: {context}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""

# 2. Build LCEL Chain
llm_chain = prompt | llm | StrOutputParser()
rag_chain = {"context": retriever, "question": RunnablePassthrough()} | llm_chain

# 3. Query the Knowledge Base
answer = rag_chain.invoke("O que a pandemia do Covid-19 gerou no desenvolvimento digital?")
print(answer)

```

---

## 💬 Sample Queries & Responses

* **Query 1:** *"O que a pandemia do Covid-19 gerou no desenvolvimento digital?"*


**Generated Answer:** A pandemia do Covid-19 gerou um impulso significativo no desenvolvimento digital, acelerando a transição de reuniões, consultas médicas e interações cotidianas para o ambiente online, além de evidenciar a escassez de profissionais qualificados em competências digitais.


* **Query 2:** *"Quanto as principais economias do mundo podem perder até 2028 em crescimento potencial?"*


**Generated Answer:** Com base no contexto fornecido pela Accenture, a estimativa é de que a lacuna de habilidades possa gerar uma perda potencial de até US$ 11,5 trilhões em crescimento econômico global até 2028.



---

## 📚 Acknowledgments & References

* Project developed as part of coursework at [Data Science Academy](https://www.datascienceacademy.com.br).


* Document ingestion powered by [Unstructured.io](https://unstructured.io/).


* Embeddings powered by [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3).


* Base LLM provided by [Meta via Hugging Face (`meta-llama/Meta-Llama-3-8B-Instruct`)](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct).



```

```