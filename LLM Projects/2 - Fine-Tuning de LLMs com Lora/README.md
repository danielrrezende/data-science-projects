# Fine-Tuning Eficiente de LLMs com LoRA e QLoRA para Análise de Sentimentos

Um projeto abrangente que demonstra o fine-tuning eficiente em parâmetros (PEFT) de um grande modelo de linguagem (`Llama-2-7b-chat-hf`) usando **QLoRA** (Quantized Low-Rank Adaptation) e **TRL (Supervised Fine-Tuning Trainer)** para tarefas de análise de sentimentos e geração de texto.

---

## 📌 Visão Geral do Projeto

Este projeto implementa um pipeline de ponta a ponta para adaptar um LLM open-source de 7 bilhões de parâmetros em dados textuais tabulares personalizados (`dataset.csv`) usando recursos computacionais mínimos:
- **Quantização:** Carrega o modelo base em precisão de 4 bits usando `bitsandbytes` para reduzir drasticamente o uso de VRAM.
- **Configuração LoRA:** Aplica matrizes de adaptação de baixo rank direcionadas aos pesos de atenção com rank personalizado ($r=32$), alpha ($16$) e dropout.
- **Fine-Tuning Supervisionado (SFT):** Treina o modelo usando o `SFTTrainer` e o `TrainingArguments` do Hugging Face com precisão mista (`fp16`).
- **Mesclagem de Pesos e Inferência:** Mescla os pesos do adaptador LoRA treinados de volta ao modelo base e executa pipelines de geração de texto.

---

## 🛠️ Pilha Tecnológica e Requisitos

- **Linguagem:** Python 3.10+ (testado no Python 3.11.5)
- **Requisito de Hardware:** GPU com alta VRAM (testado em uma NVIDIA A100 40GB)
- **Bibliotecas Principais:**
  - `transformers` (v4.31.0)
  - `peft` (v0.4.0 - para configuração do LoRA)
  - `bitsandbytes` (v0.40.2 - para quantização de 4 bits)
  - `trl` (v0.4.7 - para o `SFTTrainer`)
  - `datasets` & `pandas`
  - `torch` & `accelerate`

---

## 🚀 Instalação e Configuração

1. **Instale as dependências necessárias:**

    ```bash
    pip install -r requirements.txt
    pip install accelerate==0.21.0 peft==0.4.0 bitsandbytes==0.40.2 transformers==4.31.0
    pip install trl==0.4.7 gradio==3.37.0 protobuf==3.20.3 scipy==1.11.1 sentencepiece==0.1.99 tokenizers==0.13.3 datasets==2.16.1 watermark
    ```

2. **Prepare o Dataset:**
    Coloque seu conjunto de dados de treinamento (`dataset.csv`) no diretório raiz.

---

## ⚙️ Hiperparâmetros e Configuração

### 1. Parâmetros do LoRA (`PeftConfig`)
- `lora_r = 32`: Rank das matrizes de atualização, equilibrando a expressividade do modelo e a eficiência do treinamento.
- `lora_alpha = 16`: Fator de escala para os pesos do LoRA.
- `lora_dropout = 0.1`: Probabilidade de dropout para evitar overfitting.
- `task_type = "CAUSAL_LM"`: Alvo de modelagem de linguagem causal.

### 2. Configuração QLoRA / BitsAndBytes
- `use_4bit = True`: Habilita a quantização de 4 bits.
- `bnb_4bit_compute_dtype = "float16"`: Tipo de dado de computação.
- `bnb_4bit_quant_type = "nf4"`: Formato de quantização Normalized Float 4.

### 3. Argumentos de Treinamento (`TrainingArguments`)
- **Épocas:** `1`
- **Tamanho do Lote (Batch Size):** `4` por dispositivo (treino e avaliação)
- **Taxa de Aprendizado (Learning Rate):** `2e-4` com um agendador de taxa de aprendizado de cosseno (cosine scheduler) e razão de aquecimento (warmup) de 3%.
- **Otimizador:** `paged_adamw_32bit`

---

## 💻 Arquitetura de Código e Fluxo de Execução


```

[ dataset.csv ] ──► load_dataset() ──► DatasetDict (train)
│
[ NousResearch/Llama-2-7b-chat-hf ] ──► Quantização de 4 bits BitsAndBytes
│
▼
[ LoraConfig ] ◄── Modelo Base + Adaptadores LoRA ──► SFTTrainer
│
▼
[ Treinamento (dsa_trainer.train()) ]
│
▼
[ Salvar Adaptador e Mesclar com o Modelo Base ]
│
▼
[ Inferência / Geração por Pipeline ]

```

---

## 📊 Resultados de Treinamento e Exemplo de Inferência

- **Total de Passos de Treinamento:** 4.265
- **Perda Média de Treinamento (Training Loss):** ~2.21
- **Tempo de Treinamento:** ~30 minutos em uma GPU NVIDIA A100-SXM4-40GB.

### Prompt de Exemplo e Geração
**Prompt de Entrada:**
```python
prompt = "It's rare that a movie lives up to its hype, even rarer that the hype is transcended by the actual achievement"

```

**Saída do Modelo Ajustado (Após mesclar os pesos):**

```text
[INST] It's rare that a movie lives up to its hype, even rarer that the hype is transcended by the actual achievement [/INST] Positive:
  * The movie is visually stunning, with a unique and captivating style.
  * The story is engaging and thought-provoking, with a strong emotional impact.
  * The acting is superb, with a standout performance from Joaquin Phoenix.
  * The movie is well-written and well-directed, with a strong sense of pacing and tone.
  * The movie is a powerful and moving experience, with a strong emotional impact.
  * The movie is a must-see for fans of the genre, and for anyone who appreciates a well-crafted film.
  * The movie is a great example of the power of cinema, and the ability of filmmakers to create

```

---

## 📚 Agradecimentos e Referências

* Modelo base pré-treinado hospedado por [NousResearch / Hugging Face](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf).



<br>
<br>

---

<br>
<br>

## English
<br>

# Efficient Fine-Tuning of LLMs with LoRA & QLoRA for Sentiment Analysis

A comprehensive project demonstrating parameter-efficient fine-tuning (PEFT) of a large language model (`Llama-2-7b-chat-hf`) using **QLoRA** (Quantized Low-Rank Adaptation) and **TRL (Supervised Fine-Tuning Trainer)** for text sentiment analysis and text generation tasks.

---

## 📌 Project Overview

This project implements an end-to-end pipeline to adapt an open-source 7B parameter LLM on custom tabular text data (`dataset.csv`) using minimal computational resources:
- **Quantization:** Loads the base model in 4-bit precision using `bitsandbytes` to radically reduce VRAM usage.
- **LoRA Configuration:** Applies low-rank adaptation matrices targeting attention weights with customized rank ($r=32$), alpha ($16$), and dropout.
- **Supervised Fine-Tuning (SFT):** Trains the model using Hugging Face's `SFTTrainer` and `TrainingArguments` with mixed-precision (`fp16`).
- **Weight Merging & Inference:** Merges the trained LoRA adapter weights back into the base model and executes text generation pipelines.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+ (tested on Python 3.11.5)
- **Hardware Requirement:** GPU with high VRAM (tested on NVIDIA A100 40GB)
- **Key Libraries:**
  - `transformers` (v4.31.0)
  - `peft` (v0.4.0 - for LoRA setup)
  - `bitsandbytes` (v0.40.2 - for 4-bit quantization)
  - `trl` (v0.4.7 - for `SFTTrainer`)
  - `datasets` & `pandas`
  - `torch` & `accelerate`

---

## 🚀 Installation & Setup

1. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   pip install accelerate==0.21.0 peft==0.4.0 bitsandbytes==0.40.2 transformers==4.31.0
   pip install trl==0.4.7 gradio==3.37.0 protobuf==3.20.3 scipy==1.11.1 sentencepiece==0.1.99 tokenizers==0.13.3 datasets==2.16.1 watermark
   ```

2. **Prepare Dataset:**
   Place your training dataset (`dataset.csv`) in the root directory.

---

## ⚙️ Hyperparameters & Configuration

### 1. LoRA Parameters (`PeftConfig`)
- `lora_r = 32`: Rank of the update matrices, balancing model expressiveness and training efficiency.
- `lora_alpha = 16`: Scaling factor for LoRA weights.
- `lora_dropout = 0.1`: Dropout probability to prevent overfitting.
- `task_type = "CAUSAL_LM"`: Causal language modeling target.

### 2. QLoRA / BitsAndBytes Config
- `use_4bit = True`: Enables 4-bit quantization.
- `bnb_4bit_compute_dtype = "float16"`: Computation data type.
- `bnb_4bit_quant_type = "nf4"`: Normalized Float 4 quantization format.

### 3. Training Arguments (`TrainingArguments`)
- **Epochs:** `1`
- **Batch Size:** `4` per device (train & eval)
- **Learning Rate:** `2e-4` with a cosine learning rate scheduler and 3% warmup ratio.
- **Optimizer:** `paged_adamw_32bit`

---

## 💻 Code Architecture & Execution Flow

```
[ dataset.csv ] ──► load_dataset() ──► DatasetDict (train)
                                              │
[ NousResearch/Llama-2-7b-chat-hf ] ──► BitsAndBytes 4-bit Quantization
                                              │
                                              ▼
[ LoraConfig ] ◄── Base Model + LoRA Adapters ──► SFTTrainer
                                              │
                                              ▼
                        [ Training (dsa_trainer.train()) ]
                                              │
                                              ▼
                        [ Save Adapter & Merge with Base Model ]
                                              │
                                              ▼
                        [ Pipeline Inference / Generation ]
```

---

## 📊 Training Results & Inference Example

- **Total Training Steps:** 4,265
- **Average Training Loss:** ~2.21
- **Training Time:** ~30 minutes on an NVIDIA A100-SXM4-40GB GPU.

### Sample Prompt & Generation
**Input Prompt:**
```python
prompt = "It's rare that a movie lives up to its hype, even rarer that the hype is transcended by the actual achievement"
```

**Fine-Tuned Model Output (After merging weights):**
```text
[INST] It's rare that a movie lives up to its hype, even rarer that the hype is transcended by the actual achievement [/INST] Positive:
  * The movie is visually stunning, with a unique and captivating style.
  * The story is engaging and thought-provoking, with a strong emotional impact.
  * The acting is superb, with a standout performance from Joaquin Phoenix.
  * The movie is well-written and well-directed, with a strong sense of pacing and tone.
  * The movie is a powerful and moving experience, with a strong emotional impact.
  * The movie is a must-see for fans of the genre, and for anyone who appreciates a well-crafted film.
  * The movie is a great example of the power of cinema, and the ability of filmmakers to create
```

---

## 📚 Acknowledgments & References
- Pretrained base model hosted by [NousResearch / Hugging Face](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf).
