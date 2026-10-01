# Fine-Tuning de LLM Open-Source para Chatbot de Atendimento ao Cliente (`tiiuae/falcon-7b`)

Um projeto de ponta a ponta, documentado no notebook `lm-open-source-para-aplicativo.ipynb`, que demonstra fine-tuning eficiente em parâmetros (PEFT) usando **LoRA (Low-Rank Adaptation)** e quantização de 4 bits (`bitsandbytes`) em um grande modelo de linguagem causal (`tiiuae/falcon-7b`) para uma aplicação de chatbot de atendimento ao cliente.

---

## 📌 Visão Geral do Projeto

Este projeto implementa fine-tuning sobre um conjunto de dados personalizado de atendimento ao cliente (`dataset.json`, com 5 exemplos de treino e 1 de teste após divisão de 15%):

* **Quantização de 4 bits (`BitsAndBytesConfig`):** Carrega o modelo massivo `falcon-7b` em precisão NF4 de 4 bits com dupla quantização e offload de CPU ativado (`llm_int8_enable_fp32_cpu_offload=True`) para se ajustar às restrições de hardware.


* **Configuração LoRA (`LoraConfig`):** Congela os pesos originais do modelo e introduz adaptadores de baixo rank treináveis ($r=16, \text{alpha}=32$, dropout de $0.05$).


* **Preparação de Dados:** Analisa perguntas e respostas de clientes a partir de um JSON, formata-os em uma sequência unificada de treinamento (`question ->: answer`) e tokeniza os textos.


* **Treinamento e Avaliação:** Utiliza o `Trainer` do Hugging Face com gradient checkpointing ativado, precisão mista (`fp16=True`) e avalia a qualidade da geração usando o pacote **BLEU**.



---

## 🛠️ Pilha Tecnológica e Requisitos

* **Linguagem:** Python 3.12.3


* **Requisito de Hardware:** 2x GPUs NVIDIA Tesla T4 (Total de ~15.6 GB de VRAM por placa)


* **Bibliotecas Principais:**
* `transformers` (v4.54.0) e `peft` (v0.16.0)


* `bitsandbytes` (v0.46.1)


* `datasets` (v4.0.0)


* `accelerate` (v1.9.0) e `evaluate`




---

## 🚀 Instalação e Configuração

1. **Instale os pacotes necessários:**
```bash
pip install -q bitsandbytes==0.46.1 datasets==4.0.0 accelerate==1.9.0 loralib evaluate
pip install -q transformers==4.54.0 peft==0.16.0

```
2. **Prepare o Dataset:**
Certifique-se de que o seu arquivo JSON (`dataset.json`) contendo as perguntas e respostas de atendimento ao cliente esteja acessível e no formato correto.

## ⚙️️ Hiperparâmetros e Configuração

### 1. Configuração de Quantização (`BitsAndBytesConfig`)

* `load_in_4bit = True`

* `bnb_4bit_compute_dtype = torch.float16`

* `bnb_4bit_quant_type = "nf4"`

* `bnb_4bit_use_double_quant = True`

* `llm_int8_enable_fp32_cpu_offload = True`

### 2. Parâmetros do LoRA (`LoraConfig`)

* `r = 16`

* `lora_alpha = 32`

* `lora_dropout = 0.05`

* `task_type = "CAUSAL_LM"`

* **Parâmetros Treináveis:** 4.718.592 de 3.613.463.424 parâmetros totais (~0,13%).



### 3. Argumentos de Treinamento (`TrainingArguments`)

* **Épocas:** `10`

* **Tamanho do Lote (Batch Size):** `2` por dispositivo


* **Passos de Acumulação de Gradiente:** `2`

* **Taxa de Aprendizado (Learning Rate):** `2e-4`

* **Precisão Mista:** `fp16 = True`


---

## 💻 Arquitetura de Código e Fluxo de Execução

```text
[ dataset.json ] ──► Análise JSON ──► Dataset Hugging Face (divisão treino/teste)
                    │
[ tiiuae/falcon-7b ] ──► Quantização de 4 bits (bitsandbytes)
                    │
                    ▼
[ LoraConfig ] ◄── Congelar Base / Adicionar Adaptadores ──► Trainer (Hugging Face)
                    │
                    ▼
          [ Treinamento e Avaliação da Métrica BLEU ]
                    │
                    ▼
          [ Inferência do Chatbot / Consulta de Implantação ]

```

---

## 📊 Resultados de Treinamento e Avaliação

* **Perda de Treinamento (Training Loss Final):** Reduzida para ~1.5863 na época 10.


* **Perda de Validação (Eval Loss):** ~1.4997 na época 10.


* **Pontuação BLEU:** Avaliada na divisão de teste com pontuação BLEU de aproximadamente **0.2233** (Precisão de unigramas: 39%).



### Exemplo de Inferência

**Consulta do Usuário:**

```python
nova_pergunda_usuario = 'Como posso criar uma conta?'
```

**Resposta do Modelo (Autocast FP16):**
```text
Como posso criar uma conta?
- Clique no botão "Criar conta" no topo direito da página.
- Você será redirecionado para a página de cadastro.
- Você será redirecionado para a página de cad
```

---

## 📚 Agradecimentos e Referências

* Modelo base fornecido pela [TII UAE](https://huggingface.co/tiiuae/falcon-7b)


<br>
<br>

---

<br>
<br>

## English
<br>

# Fine-Tuning Open-Source LLM for Customer Service Chatbot (`tiiuae/falcon-7b`)

An end-to-end project, documented in the notebook `lm-open-source-para-aplicativo.ipynb`, demonstrating parameter-efficient fine-tuning (PEFT) using **LoRA (Low-Rank Adaptation)** and 4-bit quantization (`bitsandbytes`) on a causal language model (`tiiuae/falcon-7b`) for a customer service chatbot application

---

## 📌 Project Overview

This project implements fine-tuning over a custom customer service dataset (`dataset.json`, yielding 5 training samples and 1 test sample via a 15% split)
- **4-bit Quantization (`BitsAndBytesConfig`):** Loads the massive `falcon-7b` model in 4-bit NF4 precision with double quantization and CPU offload enabled (`llm_int8_enable_fp32_cpu_offload=True`) to fit GPU hardware constraints
- **LoRA Configuration (`LoraConfig`):** Freezes original model weights and introduces trainable low-rank adaptation adapters ($r=16, \text{alpha}=32$, dropout $0.05$)
- **Dataset Preparation:** Parses customer questions and answers from JSON, formats them into a unified training sequence (`question ->: answer`), and tokenizes the texts
- **Training & Evaluation:** Uses Hugging Face's `Trainer` with gradient checkpointing, mixed precision (`fp16=True`), and evaluates generation quality using the **BLEU** metric toolkit

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.12.3
- **Hardware Requirement:** 2x NVIDIA Tesla T4 GPUs (~15.6 GB VRAM each)
- **Key Libraries:**
  - `transformers` (v4.54.0) & `peft` (v0.16.0)
  - `bitsandbytes` (v0.46.1)
  - `datasets` (v4.0.0)
  - `accelerate` (v1.9.0) & `evaluate`

---

## 🚀 Installation & Setup

1. **Install required packages:**
   ```bash
   pip install -q bitsandbytes==0.46.1 datasets==4.0.0 accelerate==1.9.0 loralib evaluate
   pip install -q transformers==4.54.0 peft==0.16.0
   ```

2. **Prepare Dataset:**
   Ensure your JSON file (`dataset.json`) containing customer service questions and answers is placed and accessible in the working directory

---

## ⚙️ Hyperparameters & Configuration

### 1. Quantization Configuration (`BitsAndBytesConfig`)
* `load_in_4bit = True`
* `bnb_4bit_compute_dtype = torch.float16`
* `bnb_4bit_quant_type = "nf4"`
* `bnb_4bit_use_double_quant = True`
* `llm_int8_enable_fp32_cpu_offload = True`

### 2. LoRA Parameters (`LoraConfig`)
* `r = 16`
* `lora_alpha = 32`
* `lora_dropout = 0.05`
* `task_type = "CAUSAL_LM"`
* **Trainable Parameters:** 4,718,592 out of 3,613,463,424 total parameters (~0.13%)

### 3. Training Arguments (`TrainingArguments`)
* **Epochs:** `10`
* **Batch Size:** `2` per device
* **Gradient Accumulation Steps:** `2`
* **Learning Rate:** `2e-4`
* **Mixed Precision:** `fp16 = True`

---

## 💻 Code Architecture & Execution Flow

```text
[ dataset.json ] ──► JSON Parse ──► Hugging Face Dataset (train/test split)
                    │
[ tiiuae/falcon-7b ] ──► 4-bit Quantization (bitsandbytes)
                    │
                    ▼
[ LoraConfig ] ◄── Freeze Base / Add Adapters ──► Trainer (Hugging Face)
                    │
                    ▼
           [ Training & BLEU Metric Evaluation ]
                    │
                    ▼
           [ Chatbot Inference / Deployment Query ]

```

---

## 📊 Training Results & Evaluation

* **Final Training Loss:** Decreased to ~1.5863 at epoch 10.


* **Eval Loss:** ~1.4997 at epoch 10.


* **BLEU Score:** Evaluated on the test split, yielding a BLEU score of roughly **0.2233** (Unigram precision: 39%).



### Sample Inference Example

**User Query:**

```python
nova_pergunda_usuario = 'Como posso criar uma conta?'
```

**Model Response (FP16 Autocast):**
```text
Como posso criar uma conta?
- Clique no botão "Criar conta" no topo direito da página.
- Você será redirecionado para a página de cadastro.
- Você será redirecionado para a página de cad
```

---

## 📚 Acknowledgments & References

* Base model provided by [TII UAE](https://huggingface.co/tiiuae/falcon-7b)
