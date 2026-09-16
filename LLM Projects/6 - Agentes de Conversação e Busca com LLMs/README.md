# Agente Conversacional e de Pesquisa Web com Streamlit e LangChain

Uma aplicação web interativa de IA conversacional implantada com **Streamlit** e alimentada por **LangChain**, **OpenAI GPT** e **DuckDuckGo Search**. O agente mantém o contexto da conversa e aciona dinamicamente buscas ativas na internet para responder a consultas complexas em tempo real.

---

## 📌 Visão Geral do Projeto

Esta aplicação une Grandes Modelos de Linguagem à recuperação web em tempo real por meio de uma interface de usuário intuitiva:

* **Interface Interativa (UI):** Construída com elementos de chat do Streamlit (`st.chat_message`, `st.chat_input`), avatares personalizados e campo de credenciais na barra lateral.
* **Memória Conversacional:** Persiste as interações do chat entre as sessões do usuário usando `StreamlitChatMessageHistory` e `ConversationBufferMemory`.
* **Agente de Pesquisa ReAct:** Implementa o `ConversationalChatAgent` equipado com o `DuckDuckGoSearchRun` para decidir quando a recuperação de pesquisa externa é necessária.
* **Transparência no Processo de Pensamento:** Utiliza o `StreamlitCallbackHandler` para renderizar rastreamentos em tempo real expansíveis (`st.expander`), detalhando chamadas de ferramentas, entradas e resultados de pesquisas intermediárias.

---

## 🛠️ Pilha Tecnológica e Requisitos

* **Linguagem:** Python 3.10+
* **Frontend / Framework:** `streamlit`
* **Orquestração e Agentes:** `langchain`, `langchain-community`, `langchain-openai`
* **Ferramenta de Pesquisa:** `duckduckgo-search`
* **Provedor de LLM:** API da OpenAI (`ChatOpenAI`)

---

## 🚀 Instalação e Configuração

1. **Clone o repositório e instale as dependências:**
```bash
pip install streamlit langchain langchain-community langchain-openai duckduckgo-search requests


```



```

2. **Execute a Aplicação Streamlit:**
```bash
streamlit run app.py


```

3. **Forneça a Chave da API:**
Abra a aplicação no seu navegador e insira sua **Chave de API da OpenAI** no campo de entrada da barra lateral.

---

## 📂 Arquitetura e Fluxo de Trabalho

```
[ Entrada do Usuário via Streamlit UI ]
               │
               ▼
[ AgentExecutor (ConversationalChatAgent) ] ◄──► [ ConversationBufferMemory ]
               │
      Precisa de Pesquisa Web?
     ┌─────────┴─────────┐
    SIM                  NÃO
     │                   │
     ▼                   ▼
[ DuckDuckGo Search ]    │
     │                   │
     └─────────┬─────────┘
               │
               ▼
[ Modelo de Chat OpenAI (Streaming) ]
               │
               ▼
[ StreamlitCallbackHandler ] ──► Renderiza Processo de Pensamento e Logs de Busca
               │
               ▼
[ Resposta Final Exibida no Chat ]


```

---

## 💻 Funcionalidades e Detalhes de Implementação

* **Log de Ferramentas em Tempo Real:** Cada ação de pesquisa executada pelo agente é armazenada em `st.session_state.steps` e exibida por meio de um expansor interativo que mostra as consultas exatas e os trechos recuperados.
* **Redefinição de Conversa:** Um botão de **Redefinir (Reset)** na barra lateral limpa o histórico da conversa e restaura os estados padrão do sistema.
* **Tratamento de Erros:** Configurado com `handle_parsing_errors=True` no `AgentExecutor` para recuperar-se com elegância de discrepâncias de análise durante as etapas de raciocínio do LLM.

---

## 📚 Agradecimentos e Referências

* Framework de agentes impulsionado por [LangChain](https://python.langchain.com/).
* Interface de usuário impulsionada por [Streamlit](https://streamlit.io/).


<br>
<br>

---

<br>
<br>

## English
<br>

# Conversational & Web Search Agent with Streamlit and LangChain

An interactive conversational AI web application deployed with **Streamlit** and powered by **LangChain**, **OpenAI GPT**, and **DuckDuckGo Search**. The agent maintains conversation context and dynamically triggers live internet searches to answer complex, real-time queries.

---

## 📌 Project Overview

This application bridges Large Language Models with live web retrieval in an intuitive user interface:
- **Interactive UI:** Built with Streamlit chat elements (`st.chat_message`, `st.chat_input`), customized avatars, and sidebar credentials input.
- **Conversational Memory:** Persists chat interactions across user sessions using `StreamlitChatMessageHistory` and `ConversationBufferMemory`.
- **ReAct Search Agent:** Implements `ConversationalChatAgent` equipped with `DuckDuckGoSearchRun` to decide when external search retrieval is necessary.
- **Thought Process Transparency:** Uses `StreamlitCallbackHandler` to render expandable real-time traces (`st.expander`), detailing tool invocations, inputs, and intermediate search results.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+
- **Frontend / Framework:** `streamlit`
- **Orchestration & Agents:** `langchain`, `langchain-community`, `langchain-openai`
- **Search Tool:** `duckduckgo-search`
- **LLM Provider:** OpenAI API (`ChatOpenAI`)

---

## 🚀 Installation & Setup

1. **Clone the repository and install dependencies:**

   ```bash
   pip install streamlit langchain langchain-community langchain-openai duckduckgo-search requests

```

2. **Run the Streamlit Application:**
```bash
streamlit run app.py

```


3. **Provide API Key:**
Open the application in your browser and enter your **OpenAI API Key** in the sidebar input field.

---

## 📂 Architecture & Workflow

```
[ User Input via Streamlit UI ]
               │
               ▼
[ AgentExecutor (ConversationalChatAgent) ] ◄──► [ ConversationBufferMemory ]
               │
      Needs Web Search?
     ┌─────────┴─────────┐
    YES                  NO
     │                   │
     ▼                   ▼
[ DuckDuckGo Search ]    │
     │                   │
     └─────────┬─────────┘
               │
               ▼
[ OpenAI Chat Model (Streaming) ]
               │
               ▼
[ StreamlitCallbackHandler ] ──► Renders Thought Process & Search Logs
               │
               ▼
[ Final Response Displayed in Chat ]

```

---

## 💻 Features & Implementation Details

* **Live Tool Logging:** Each search action executed by the agent is stored inside `st.session_state.steps` and displayed through an interactive expander showing exact queries and retrieved snippets.
* **Conversation Reset:** A convenient **Reset** button in the sidebar wipes conversational history and reinstates default system states.
* **Error Handling:** Configured with `handle_parsing_errors=True` in `AgentExecutor` to gracefully recover from parsing discrepancies during LLM reasoning steps.

---

## 📚 Acknowledgments & References

* Agent framework powered by [LangChain](https://python.langchain.com/).
* UI powered by [Streamlit](https://streamlit.io/).
