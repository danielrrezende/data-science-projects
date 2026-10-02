# Criando Aplicações Inteligentes com LangChain e LLMs

Um projeto prático focado no desenvolvimento de aplicações de Inteligência Artificial utilizando grandes modelos de linguagem (LLMs) da OpenAI orquestrados pelo framework LangChain. O notebook demonstra a implementação de fluxos de trabalho inteligentes, abrangendo desde templates de prompt básicos até sistemas de Recuperação Aumentada por Geração (RAG) com bancos de dados vetoriais e agentes de conversação com memória.

---

## 📌 Visão Geral do Projeto

Este projeto serve como um guia abrangente para recursos do LangChain, implementando os seguintes cenários e técnicas:

* **Prompt Templates e LLMChains:** Criação de prompts dinâmicos para geração de nomes de restaurantes e itens de menu personalizados (ex: culinária Italiana, Mexicana, Indiana).


* **Encadeamento Sequencial:** Uso de `SimpleSequentialChain` e `SequentialChain` para conectar a saída de uma chamada de LLM como entrada para a próxima.


* **Gerenciamento de Memória:** Implementação de `ConversationBufferMemory` e `ConversationBufferWindowMemory` dentro de uma `ConversationChain` para construir um assistente capaz de lembrar o contexto da conversa (demonstrado em um Q&A sobre a Copa do Mundo).


* **Pipeline RAG (Retrieval-Augmented Generation):** Extração de dados da web (`WebBaseLoader`), vetorização com `OpenAIEmbeddings` e armazenamento no `Chroma` VectorDB para responder a perguntas contextuais usando a classe `RetrievalQA`.


* **Chatbot Baseado em Personagem:** Criação de um chatbot de linha de comando simulando um especialista em vendas de carros esportivos.



---

## 🛠️ Pilha Tecnológica e Requisitos

* **Linguagem:** Python 3.11.5.


* **Modelos de Linguagem:** `OpenAI` e `ChatOpenAI`.


* **Bibliotecas e Frameworks Principais:**
* `langchain==0.1.13` e `langchain-community`.


* `langchain-openai==0.1.1`.


* `chromadb==0.4.24` (para o banco de dados vetorial).


* `sqlalchemy==2.0.29`.





---

## 🚀 Instalação e Configuração

1. **Instale os pacotes necessários:**
```bash
pip install -q -U langchain-openai==0.1.1
pip install -q -U langchain-community
pip install -q -U chromadb==0.4.24
pip install -q -U sqlalchemy==2.0.29
pip install -q -U langchain==0.1.13


```


2. **Configuração de Ambiente:**
O projeto requer uma chave de API válida da OpenAI definida nas variáveis de ambiente:
```python
import os
from google.colab import userdata
os.environ['OPENAI_API_KEY'] = userdata.get('OPENAI_API_KEY')


```



---

## 💻 Fluxos de Execução Destacados

### 1. Sequential Chains (Cadeias Sequenciais)

Permite executar componentes de forma condicional e dinâmica.

* **Passo 1:** O modelo sugere o nome de um restaurante com base no tipo de culinária.


* **Passo 2:** O modelo recebe o nome gerado e sugere um menu apropriado para o local.



### 2. Pipeline RAG com ChromaDB

* **Extração:** Obtém o conteúdo de um blog usando `WebBaseLoader`.


* **Indexação:** Converte o texto em `OpenAIEmbeddings` e o salva no `Chroma` VectorDB.


* **Recuperação e Geração:** Utiliza `RetrievalQA` e o retriever do banco de dados (limitado ao top 1 resultado) para responder perguntas sobre o que é RAG de forma fundamentada.



---

## 📊 Exemplo de Inferência: Pipeline RAG

**Consulta Submetida:**

```python
query = "Explique o que é RAG em 5 sentenças"
resposta = chain.invoke(query)
```

**Resposta do Sistema:**
```text
RAG é uma abordagem que combina geração de texto com recuperação de informações para personalizar modelos de linguagem de grande escala (LLMs). Ele utiliza um mecanismo de busca para recuperar informações relevantes que são incorporadas na geração de texto, melhorando a qualidade e relevância das respostas geradas. Essa abordagem permite que os LLMs sejam mais precisos e contextualmente relevantes, tornando a interação com sistemas de IA mais natural e eficaz. RAG é especialmente útil em tarefas de geração de texto que exigem conhecimento específico ou contextualização, como respostas a perguntas ou produção de conteúdo personalizado. Essa técnica está se tornando cada vez mais popular na comunidade de IA devido aos seus benefícios em melhorar a capacidade dos modelos de linguagem de entender e gerar texto de forma mais inteligente.
```


<br>
<br>

---

<br>
<br>

## English
<br>

# Building Intelligent Applications with LangChain and LLMs

A hands-on project focused on developing AI applications using OpenAI's Large Language Models (LLMs) orchestrated by the LangChain framework. The notebook demonstrates the implementation of intelligent workflows, ranging from basic prompt templates to Retrieval-Augmented Generation (RAG) systems with vector databases and conversational memory agents.

---

## 📌 Project Overview

This project serves as a comprehensive guide to LangChain features, implementing the following scenarios and techniques:
*   **Prompt Templates & LLMChains:** Creating dynamic prompts for generating personalized restaurant names and menu items (e.g., Italian, Mexican, Indian cuisine).
*   **Sequential Chaining:** Using `SimpleSequentialChain` and `SequentialChain` to pipe the output of one LLM call directly as the input to the next.
*   **Memory Management:** Implementing `ConversationBufferMemory` and `ConversationBufferWindowMemory` inside a `ConversationChain` to build an assistant that retains conversational context (demonstrated through a World Cup Q&A).
*   **RAG Pipeline:** Extracting web data (`WebBaseLoader`), vectorizing it via `OpenAIEmbeddings`, and storing it in a `Chroma` VectorDB to answer contextual questions using the `RetrievalQA` class.
*   **Persona-Based Chatbot:** Building an interactive command-line chatbot simulating a sports car sales specialist.

---

## 🛠️ Tech Stack & Requirements

*   **Language:** Python 3.11.5.
*   **Language Models:** `OpenAI` and `ChatOpenAI`.
*   **Key Libraries & Frameworks:**
    *   `langchain==0.1.13` and `langchain-community`.
    *   `langchain-openai==0.1.1`.
    *   `chromadb==0.4.24` (for vector database functionality).
    *   `sqlalchemy==2.0.29`.

---

## 🚀 Installation & Setup

1.  **Install the required packages:**
    ```bash
    pip install -q -U langchain-openai==0.1.1
    pip install -q -U langchain-community
    pip install -q -U chromadb==0.4.24
    pip install -q -U sqlalchemy==2.0.29
    pip install -q -U langchain==0.1.13
    ```

2.  **Environment Setup:**
    The project requires a valid OpenAI API Key defined in the environment variables:
    ```python
    import os
    from google.colab import userdata
    os.environ['OPENAI_API_KEY'] = userdata.get('OPENAI_API_KEY')
    ```

---

## 💻 Highlighted Execution Flows

### 1. Sequential Chains
Allows for dynamic and conditional execution of components.
*   **Step 1:** The model suggests a restaurant name based on a cuisine type input.
*   **Step 2:** The model takes the generated name and suggests an appropriate menu for the establishment.

### 2. RAG Pipeline with ChromaDB
*   **Extraction:** Scrapes a blog post content using `WebBaseLoader`.
*   **Indexing:** Converts the text into `OpenAIEmbeddings` and saves it into the `Chroma` VectorDB.
*   **Retrieval & Generation:** Uses `RetrievalQA` and the DB retriever (capped at the top 1 result) to deliver grounded answers regarding how RAG works.

---

## 📊 Inference Example: RAG Pipeline

**Submitted Query:**
```python
query = "Explique o que é RAG em 5 sentenças"
resposta = chain.invoke(query)
```

**System Response:**
```text
RAG é uma abordagem que combina geração de texto com recuperação de informações para personalizar modelos de linguagem de grande escala (LLMs). Ele utiliza um mecanismo de busca para recuperar informações relevantes que são incorporadas na geração de texto, melhorando a qualidade e relevância das respostas geradas. Essa abordagem permite que os LLMs sejam mais precisos e contextualmente relevantes, tornando a interação com sistemas de IA mais natural e eficaz. RAG é especialmente útil em tarefas de geração de texto que exigem conhecimento específico ou contextualização, como respostas a perguntas ou produção de conteúdo personalizado. Essa técnica está se tornando cada vez mais popular na comunidade de IA devido aos seus benefícios em melhorar a capacidade dos modelos de linguagem de entender e gerar texto de forma mais inteligente.
```
