# Fine-Tuning Eficiente de LLMs com LoRA e QLoRA para Análise de Sentimentos

Um projeto abrangente que demonstra o fine-tuning eficiente em parâmetros (PEFT) de um grande modelo de linguagem (`Llama-2-7b-chat-hf`)[cite: 1] usando **QLoRA** (Quantized Low-Rank Adaptation) e **TRL (Supervised Fine-Tuning Trainer)** para tarefas de análise de sentimentos e geração de texto[cite: 1].

---

## 📌 Visão Geral do Projeto

Este projeto implementa um pipeline de ponta a ponta para adaptar um LLM open-source de 7 bilhões de parâmetros em dados textuais tabulares personalizados (`dataset.csv` contendo 17.057 exemplos no particionamento de treino)[cite: 1] usando recursos computacionais mínimos:
- **Quantização:** Carrega o modelo base em precisão de 4 bits usando `bitsandbytes` para reduzir drasticamente o uso de VRAM[cite: 1].
- **Configuração LoRA:** Aplica matrizes de adaptação de baixo rank direcionadas aos pesos de atenção com rank personalizado ($r=32$), alpha ($16$) e dropout ($0.1$)[cite: 1].
- **Fine-Tuning Supervisionado (SFT):** Treina o modelo usando o `SFTTrainer` e o `TrainingArguments` do Hugging Face[cite: 1].
- **Mesclagem de Pesos e Inferência:** Mescla os pesos do adaptador LoRA treinados de volta ao modelo base e executa pipelines de geração de texto[cite: 1].

---

## 🛠️ Pilha Tecnológica e Requisitos

- **Linguagem:** Python 3.12.13[cite: 1]
- **Requisito de Hardware:** GPU (testado em uma NVIDIA Tesla T4 com aproximadamente 15.6 GB de VRAM)[cite: 1]
- **Bibliotecas Principais (Versões Atualizadas):**
  - `transformers` (v4.54.0)[cite: 1]
  - `peft` (v0.16.0 - para configuração do LoRA)[cite: 1]
  - `bitsandbytes` (v0.46.1 - para quantização de 4 bits)[cite: 1]
  - `trl` (v0.20.0 - para o `SFTTrainer`)[cite: 1]
  - `torch` (v2.10.0) & `datasets` (v4.0.0)[cite: 1]
  - `pandas` (v2.2.2)[cite: 1]

---

## 🚀 Instalação e Configuração

1. **Instale as dependências necessárias fixando as versões adequadas:**

    ```bash
    pip install torch==2.10.0
    pip install transformers==4.54.0 pandas==2.2.2 tokenizers==0.21.2 accelerate==1.9.0 trl==0.20.0 peft==0.16.0 bitsandbytes==0.46.1 scipy==1.16.0 sentencepiece==0.2.0 numba==0.60.0 gradio==5.38.2 datasets==4.0.0 watermark
    ```[cite: 1]

2. **Prepare o Dataset:**
    Coloque seu conjunto de dados de treinamento (`dataset.csv`) no diretório raiz ou referencie seu respectivo caminho no código[cite: 1].

---

## ⚙️ Hiperparâmetros e Configuração

### 1. Parâmetros do LoRA (`PeftConfig`)
- `lora_r = 32`: Rank das matrizes de atualização, equilibrando a expressividade do modelo e a eficiência do treinamento[cite: 1].
- `lora_alpha = 16`: Fator de escala para os pesos do LoRA[cite: 1].
- `lora_dropout = 0.1`: Probabilidade de dropout para evitar overfitting[cite: 1].
- `task_type = "CAUSAL_LM"`: Alvo de modelagem de linguagem causal[cite: 1].

### 2. Configuração QLoRA / BitsAndBytes
- `use_4bit = True`: Habilita a quantização de 4 bits[cite: 1].
- `bnb_4bit_compute_dtype = "float16"`: Tipo de dado de computação[cite: 1].
- `bnb_4bit_quant_type = "nf4"`: Formato de quantização Normalized Float 4[cite: 1].
- `use_nested_quant = False`: Desativa quantização aninhada[cite: 1].

### 3. Argumentos de Treinamento (`SFTConfig`)
- **Épocas:** `1`[cite: 1].
- **Tamanho do Lote (Batch Size):** `2` por dispositivo (reduzido para suportar o ambiente de treinamento)[cite: 1].
- **Passos de Acumulação de Gradiente:** `4` (aumentado para compensar a redução do batch size)[cite: 1].
- **Taxa de Aprendizado (Learning Rate):** `2e-4` com um agendador de taxa de aprendizado de cosseno (cosine scheduler) e razão de aquecimento (warmup) de 3%[cite: 1].
- **Otimizador:** `paged_adamw_32bit`[cite: 1].

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
[ Treinamento (tf_trainer.train()) ]
│
▼
[ Salvar Adaptador e Mesclar com o Modelo Base ]
│
▼
[ Inferência / Geração por Pipeline ]

```

---

## 📊 Resultados de Treinamento e Exemplo de Inferência

- **Total de Passos de Treinamento (Global Steps):** 2.133[cite: 1].
- **Perda de Treinamento (Training Loss Final):** 4.5702[cite: 1].
- **Tempo de Treinamento:** ~11 horas e 37 minutos em uma GPU NVIDIA Tesla T4[cite: 1].

### Prompt de Exemplo e Geração
**Prompt de Entrada:**
```python
prompt = "It's rare that a movie lives up to its hype, even rarer that the hype is transcended by the actual achievement"
```[cite: 1]

**Saída do Modelo Ajustado (Após gerar os novos textos positivos/negativos da avaliação):**

```text
[INST] It's rare that a movie lives up to its hype, even rarer that the hype is transcended by the actual achievement [/INST]  I couldn't agree more! It's often the case that movies generate a lot of buzz and excitement leading up to their release, only to fall short of expectations once they hit theaters. Here are some reasons why this happens:

1. Overhyping: Sometimes, the media and fans can get carried away with the excitement surrounding a movie, building it up to be something it's not. This can create unrealistic expectations that are difficult for the movie to live up to.
2. Lack of originality: Movies that are heavily promoted and hyped often have a lot riding on them in terms of originality and creativity. If the movie doesn't deliver on these fronts, it can be a disappoint
```[cite: 1]

---

## 📚 Agradecimentos e Referências

* Modelo base pré-treinado hospedado por [NousResearch / Hugging Face](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf)[cite: 1].


<br>
<br>

---

<br>
<br>

## English
<br>

# Efficient Fine-Tuning of LLMs with LoRA & QLoRA for Sentiment Analysis

A comprehensive project demonstrating parameter-efficient fine-tuning (PEFT) of a large language model (`Llama-2-7b-chat-hf`)[cite: 1] using **QLoRA** (Quantized Low-Rank Adaptation) and **TRL (Supervised Fine-Tuning Trainer)** for text sentiment analysis and text generation tasks[cite: 1].

---

## 📌 Project Overview

This project implements an end-to-end pipeline to adapt an open-source 7B parameter LLM on custom tabular text data (`dataset.csv` holding 17,057 rows in the train split)[cite: 1] using minimal computational resources:
- **Quantization:** Loads the base model in 4-bit precision using `bitsandbytes` to radically reduce VRAM usage[cite: 1].
- **LoRA Configuration:** Applies low-rank adaptation matrices targeting attention weights with customized rank ($r=32$), alpha ($16$), and dropout ($0.1$)[cite: 1].
- **Supervised Fine-Tuning (SFT):** Trains the model using Hugging Face's `SFTTrainer` and `TrainingArguments`[cite: 1].
- **Weight Merging & Inference:** Merges the trained LoRA adapter weights back into the base model and executes text generation pipelines[cite: 1].

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.12.13[cite: 1].
- **Hardware Requirement:** GPU (tested on an NVIDIA Tesla T4 with ~15.6 GB VRAM)[cite: 1].
- **Key Libraries (Updated Versions):**
  - `transformers` (v4.54.0)[cite: 1].
  - `peft` (v0.16.0 - for LoRA setup)[cite: 1].
  - `bitsandbytes` (v0.46.1 - for 4-bit quantization)[cite: 1].
  - `trl` (v0.20.0 - for `SFTTrainer`)[cite: 1].
  - `torch` (v2.10.0) & `datasets` (v4.0.0)[cite: 1].
  - `pandas` (v2.2.2)[cite: 1].

---

## ⚙️ Hyperparameters & Configuration

### 1. LoRA Parameters (`PeftConfig`)
- `lora_r = 32`: Rank of the update matrices, balancing model expressiveness and training efficiency[cite: 1].
- `lora_alpha = 16`: Scaling factor for LoRA weights[cite: 1].
- `lora_dropout = 0.1`: Dropout probability to prevent overfitting[cite: 1].
- `task_type = "CAUSAL_LM"`: Causal language modeling target[cite: 1].

### 2. QLoRA / BitsAndBytes Config
- `use_4bit = True`: Enables 4-bit quantization[cite: 1].
- `bnb_4bit_compute_dtype = "float16"`: Computation data type[cite: 1].
- `bnb_4bit_quant_type = "nf4"`: Normalized Float 4 quantization format[cite: 1].
- `use_nested_quant = False`: Disables nested quantization[cite: 1].

### 3. Training Arguments (`SFTConfig`)
- **Epochs:** `1`[cite: 1].
- **Batch Size:** `2` per device (reduced to fit the GPU memory)[cite: 1].
- **Gradient Accumulation Steps:** `4` (increased to maintain effective speed)[cite: 1].
- **Learning Rate:** `2e-4` with a cosine learning rate scheduler and 3% warmup ratio[cite: 1].
- **Optimizer:** `paged_adamw_32bit`[cite: 1].

---

## 📊 Training Results & Inference Example

- **Total Training Steps (Global Steps):** 2,133[cite: 1].
- **Final Training Loss:** 4.5702[cite: 1].
- **Training Time:** ~11 hours and 37 minutes on an NVIDIA Tesla T4[cite: 1].

### Sample Prompt & Generation
**Input Prompt:**
```python
prompt = "It's rare that a movie lives up to its hype, even rarer that the hype is transcended by the actual achievement"
```[cite: 1]

**Fine-Tuned Model Output:**
```text
[INST] It's rare that a movie lives up to its hype, even rarer that the hype is transcended by the actual achievement [/INST]  I couldn't agree more! It's often the case that movies generate a lot of buzz and excitement leading up to their release, only to fall short of expectations once they hit theaters. Here are some reasons why this happens:

1. Overhyping: Sometimes, the media and fans can get carried away with the excitement surrounding a movie, building it up to be something it's not. This can create unrealistic expectations that are difficult for the movie to live up to.
2. Lack of originality: Movies that are heavily promoted and hyped often have a lot riding on them in terms of originality and creativity. If the movie doesn't deliver on these fronts, it can be a disappoint
```[cite: 1]

---

## 📚 Acknowledgments & References
- Pretrained base model hosted by [NousResearch / Hugging Face](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf)[cite: 1].

```
