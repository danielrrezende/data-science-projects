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

* **Live Tool Logging:** Each search action executed by the agent is stored inside `st.session_state.steps` and displayed through an interactive expander showing exact query queries and retrieved snippets.
* **Conversation Reset:** A convenient **Reset** button in the sidebar wipes conversational history and reinstates default system states.
* **Error Handling:** Configured with `handle_parsing_errors=True` in `AgentExecutor` to gracefully recover from parsing discrepancies during LLM reasoning steps.

---

## 📚 Acknowledgments & References

* Agent framework powered by [LangChain](https://python.langchain.com/).
* UI powered by [Streamlit](https://streamlit.io/).
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content_p6)

print("README.md for Projeto 6 created successfully!")

```

```text?code_stdout&code_event_index=1
README.md for Projeto 6 created successfully!


```

O arquivo **`README.md`** para a aplicação web do agente conversacional (`app.py`) foi gerado com sucesso[cite: 13]:

📥 **[Baixar README.md](https://www.google.com/search?q=sandbox:/README.md)**

---

### Conteúdo completo do arquivo:

```markdown
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

```

```
