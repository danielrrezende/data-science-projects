# Fine-Tuning de Instruções e Sistema de QA com LangChain usando LLM Open-Source (`Llama-2-7b-chat-hf`)

Uma implementação ponta a ponta de fine-tuning de instruções eficiente em parâmetros usando **QLoRA** no `Llama-2-7b-chat-hf`, seguida pela integração do modelo ajustado em um pipeline conversacional de Perguntas e Respostas alimentado pelo **LangChain**.

---

## 📌 Visão Geral do Projeto

Este projeto constrói um assistente especializado de Perguntas e Respostas voltado para um domínio específico usando o conjunto de dados `nlpie/Llama2-MedTuned-Instructions`:
- **Pré-processamento de Dados de Instrução:** Prepara prompts de fine-tuning supervisionado envolvendo a instrução, o contexto de entrada e a saída esperada no modelo de formatação de chat padrão do LLaMA-2 (`[INST]<<SYS>>...[/INST]`).
- **Fine-Tuning QLoRA de 4 Bits:** Carrega o modelo base em NormalFloat de 4 bits (`nf4`) via `bitsandbytes`, anexa adaptadores de baixo rank (`r=8, alpha=16`) com o `peft` e executa o instruction tuning por meio do `SFTTrainer` da TRL.
- **Mesclagem de Adaptadores:** Mescla os adaptadores LoRA treinados de volta aos pesos do modelo base com `merge_and_unload()` para implantação otimizada e inferência de modelo único.
- **Pipeline LangChain e Memória:** Envolve o modelo mesclado em um `HuggingFacePipeline`, estabelece um modelo de prompt com `PromptTemplate` e equipa o modelo com interação com estado usando `ConversationBufferMemory` em uma `LLMChain`.

---

## 🛠️ Pilha Tecnológica e Requisitos

- **Linguagem:** Python 3.10+ (testado no Python 3.11.5)
- **Requisito de Hardware:** GPU com suporte a CUDA (testado em uma NVIDIA A100 40GB)
- **Frameworks e Bibliotecas Principais:**
  - `transformers` & `peft`
  - `bitsandbytes` & `accelerate`
  - `trl` (para o `SFTTrainer`)
  - `datasets` (Hugging Face Datasets)
  - `langchain` & `langchain-community`
  - `watermark`

---

## 🚀 Instalação e Configuração

1. **Instale as bibliotecas necessárias:**
   ```bash
   pip install -q accelerate peft bitsandbytes transformers trl datasets langchain watermark

```

2. **Dataset:**
O notebook busca os dados diretamente do Hugging Face Hub:
* Dataset: [`nlpie/Llama2-MedTuned-Instructions`](https://huggingface.co/datasets/nlpie/Llama2-MedTuned-Instructions)
* Modelo Base: [`NousResearch/Llama-2-7b-chat-hf`](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf)



---

## ⚙️ Hiperparâmetros e Configuração

### 1. Quantização (`BitsAndBytesConfig`)

* `load_in_4bit = True`
* `bnb_4bit_compute_dtype = "float16"`
* `bnb_4bit_quant_type = "nf4"`
* `use_nested_quant = False`

### 2. Configurações LoRA (`LoraConfig`)

* `r = 8`
* `lora_alpha = 16`
* `lora_dropout = 0.05`
* `bias = "none"`
* `task_type = "CAUSAL_LM"`

### 3. Argumentos de Treinamento SFT (`TrainingArguments`)

* **Otimizador:** `paged_adamw_32bit`
* **Taxa de Aprendizado (Learning Rate):** `2e-4` (agendador de cosseno / cosine scheduler)
* **Tamanho do Lote (Batch Size):** `1` por dispositivo com `gradient_accumulation_steps = 4`
* **Passos de Treinamento:** Máximo de `150` passos com `fp16 = True`
* **Comprimento de Sequência:** `max_seq_length = 512` com empacotamento de sequência ativado (`packing = True`)

---

## 💻 Arquitetura e Fluxo de Trabalho

```
[ nlpie/Llama2-MedTuned-Instructions ]
                  │
                  ▼
[ Formatação do Modelo de Prompt Personalizado ] ──► TRL SFTTrainer
                  │                                         │
[ Llama-2-7b-chat-hf (QLoRA 4-bit) ] ───────────────────────┘
                  │
                  ▼
        [ 150 Passos de Treinamento ]
                  │
                  ▼
        [ Salvar e Mesclar Adaptador LoRA ]
                  │
                  ▼
   [ Pipeline Hugging Face ] (text-generation)
                  │
                  ▼
   [ LangChain LLMChain + ConversationBufferMemory ]
                  │
                  ▼
       [ Assistente de QA Interativo ]

```

---

## 💬 Consulta de Exemplo e Saída

**Pergunta do Usuário (Contexto):**

```text
###Question: All of the following provisions are included in the Primary health care according to the Alma Ata declaration except:
###Options:
A. Adequate supply of safe drinking water
B. Nutrition
C. Provision of free medicines
D. Basic sanitation

```

**Resposta do Assistente:**

```text
Great! Let's analyze the question and answer options:

Question: All of the following provisions are included in the Primary health care according to the Alma Ata declaration except:

Options:
A. Adequate supply of safe drinking water
B. Nutrition
C. Provision of free medicines
D. Basic sanitation

The Alma Ata declaration is a widely recognized international document that outlines the principles of primary health care. According to the declaration, primary health care should include the following provisions:

* Adequate supply of safe drinking water
* Nutrition
* Provision of free medicines
* Basic sanitation

However, the question asks about the exception, which is not included in the Alma Ata declaration. Therefore, the best answer is (D) Basic sanitation.

```

---

## 📚 Agradecimentos e Referências

* Modelo pré-treinado hospedado por [NousResearch / Hugging Face](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf).
* Conjunto de dados curado por [nlpie no Hugging Face](https://huggingface.co/datasets/nlpie/Llama2-MedTuned-Instructions).


<br>
<br>

---

<br>
<br>

## English
<br>

# Instruction Fine-Tuning & LangChain QA System with Open-Source LLM (`Llama-2-7b-chat-hf`)

An end-to-end implementation of parameter-efficient instruction fine-tuning using **QLoRA** on `Llama-2-7b-chat-hf`, followed by the integration of the fine-tuned model into a conversational Question & Answering pipeline powered by **LangChain**.

---

## 📌 Project Overview

This project builds a specialized domain-specific Question & Answering assistant using the `nlpie/Llama2-MedTuned-Instructions` dataset:
- **Instruction Data Preprocessing:** Prepares supervised fine-tuning prompts by wrapping instruction, input context, and expected output into the standard LLaMA-2 chat formatting template (`[INST]<<SYS>>...[/INST]`).
- **4-Bit QLoRA Fine-Tuning:** Loads the base model in 4-bit NormalFloat (`nf4`) via `bitsandbytes`, attaches low-rank adapters (`r=8, alpha=16`) with `peft`, and executes instruction tuning via TRL's `SFTTrainer`.
- **Adapter Merging:** Merges trained LoRA adapters back into the base model weights with `merge_and_unload()` for optimized deployment and single-model inference.
- **LangChain Pipeline & Memory:** Wraps the merged model in a `HuggingFacePipeline`, establishes a prompt template with `PromptTemplate`, and equips the model with stateful interaction using `ConversationBufferMemory` in an `LLMChain`.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+ (tested on Python 3.11.5)
- **Hardware Requirement:** GPU with CUDA support (tested on NVIDIA A100 40GB)
- **Frameworks & Key Libraries:**
  - `transformers` & `peft`
  - `bitsandbytes` & `accelerate`
  - `trl` (for `SFTTrainer`)
  - `datasets` (Hugging Face Datasets)
  - `langchain` & `langchain-community`
  - `watermark`

---

## 🚀 Installation & Setup

1. **Install required libraries:**
   ```bash
   pip install -q accelerate peft bitsandbytes transformers trl datasets langchain watermark
   ```

2. **Dataset:**
   The notebook pulls directly from the Hugging Face Hub:
   - Dataset: [`nlpie/Llama2-MedTuned-Instructions`](https://huggingface.co/datasets/nlpie/Llama2-MedTuned-Instructions)
   - Base Model: [`NousResearch/Llama-2-7b-chat-hf`](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf)

---

## ⚙️ Hyperparameters & Configuration

### 1. Quantization (`BitsAndBytesConfig`)
- `load_in_4bit = True`
- `bnb_4bit_compute_dtype = "float16"`
- `bnb_4bit_quant_type = "nf4"`
- `use_nested_quant = False`

### 2. LoRA Settings (`LoraConfig`)
- `r = 8`
- `lora_alpha = 16`
- `lora_dropout = 0.05`
- `bias = "none"`
- `task_type = "CAUSAL_LM"`

### 3. SFT Training Arguments (`TrainingArguments`)
- **Optimizer:** `paged_adamw_32bit`
- **Learning Rate:** `2e-4` (cosine scheduler)
- **Batch Size:** `1` per device with `gradient_accumulation_steps = 4`
- **Training Steps:** `150` max steps with `fp16 = True`
- **Sequence Length:** `max_seq_length = 512` with sequence packing enabled (`packing = True`)

---

## 💻 Architecture & Workflow

```
[ nlpie/Llama2-MedTuned-Instructions ]
                  │
                  ▼
[ Custom Prompt Template Formatting ] ──► TRL SFTTrainer
                  │                              │
[ Llama-2-7b-chat-hf (4-bit QLoRA) ] ────────────┘
                  │
                  ▼
       [ 150 Training Steps ]
                  │
                  ▼
       [ Save & Merge LoRA Adapter ]
                  │
                  ▼
   [ Hugging Face Pipeline ] (text-generation)
                  │
                  ▼
   [ LangChain LLMChain + ConversationBufferMemory ]
                  │
                  ▼
     [ Interactive QA Assistant ]
```

---

## 💬 Sample Query & Output

**User Question (Context):**
```text
###Question: All of the following provisions are included in the Primary health care according to the Alma Ata declaration except:
###Options:
A. Adequate supply of safe drinking water
B. Nutrition
C. Provision of free medicines
D. Basic sanitation
```

**Assistant Response:**
```text
Great! Let's analyze the question and answer options:

Question: All of the following provisions are included in the Primary health care according to the Alma Ata declaration except:

Options:
A. Adequate supply of safe drinking water
B. Nutrition
C. Provision of free medicines
D. Basic sanitation

The Alma Ata declaration is a widely recognized international document that outlines the principles of primary health care. According to the declaration, primary health care should include the following provisions:

* Adequate supply of safe drinking water
* Nutrition
* Provision of free medicines
* Basic sanitation

However, the question asks about the exception, which is not included in the Alma Ata declaration. Therefore, the best answer is (D) Basic sanitation.
```

---

## 📚 Acknowledgments & References
- Pretrained model hosted by [NousResearch / Hugging Face](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf).
- Dataset curated by [nlpie on Hugging Face](https://huggingface.co/datasets/nlpie/Llama2-MedTuned-Instructions).
