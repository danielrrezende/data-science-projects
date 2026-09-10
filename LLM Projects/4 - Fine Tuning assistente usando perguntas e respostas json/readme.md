# Fine-Tuning Open-Source LLM for Customer Service Chatbot (`tiiuae/falcon-7b`)

An end-to-end project demonstrating parameter-efficient fine-tuning (PEFT) using **LoRA (Low-Rank Adaptation)** and 4-bit quantization (`bitsandbytes`) on a causal language model (`tiiuae/falcon-7b`) for a customer service chatbot application.

---

## 📌 Project Overview

This project implements fine-tuning over a custom customer service dataset (`dataset.json`):
- **4-bit Quantization (`BitsAndBytesConfig`):** Loads the massive `falcon-7b` model in 4-bit NF4 precision with double quantization to fit standard GPU hardware constraints.
- **LoRA Configuration (`LoraConfig`):** Freezes original model weights, introduces trainable low-rank adaptation adapters ($r=16, \text{alpha}=32$), and casts output heads for stability.
- **Dataset Preparation:** Parses customer questions and answers from JSON, formats them into a unified training sequence (`question ->: answer`), and tokenizes the texts.
- **Training & Evaluation:** Uses Hugging Face's `Trainer` with gradient checkpointing, mixed precision (`fp16`), and evaluates generation quality using the **BLEU** metric toolkit.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+ (tested on Python 3.11.5)
- **Hardware Requirement:** GPU with high VRAM (tested on NVIDIA A100 40GB)
- **Key Libraries:**
  - `transformers` & `peft` (for LoRA and model wrapping)
  - `bitsandbytes` (for 4-bit NF4 quantization)
  - `datasets` (for training/test splits)
  - `evaluate` & `nltk` (for BLEU evaluation)

---

## 🚀 Installation & Setup

1. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   pip install bitsandbytes datasets accelerate loralib evaluate
   pip install git+[https://github.com/huggingface/transformers.git@main](https://github.com/huggingface/transformers.git@main) git+[https://github.com/huggingface/peft.git](https://github.com/huggingface/peft.git)


2. **Prepare Dataset:**
Ensure your JSON file (`dataset.json`) containing customer service questions and answers is placed in the working directory.

---

## ⚙️ Hyperparameters & Configuration

### 1. Quantization Configuration (`BitsAndBytesConfig`)

* `load_in_4bit = True`
* `bnb_4bit_compute_dtype = torch.float16`
* `bnb_4bit_quant_type = "nf4"`
* `bnb_4bit_use_double_quant = True`

### 2. LoRA Parameters (`LoraConfig`)

* `r = 16` (rank)
* `lora_alpha = 32` (scaling factor)
* `lora_dropout = 0.05`
* `task_type = "CAUSAL_LM"`
* **Trainable Parameters:** ~4.7 million out of 3.6 billion parameters (~0.13%)

### 3. Training Arguments (`TrainingArguments`)

* **Epochs:** `10`
* **Batch Size:** `2` per device with `gradient_accumulation_steps = 2`
* **Learning Rate:** `2e-4`
* **Mixed Precision:** `fp16 = True`

---

## 💻 Code Architecture & Execution Flow

```
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

* **Training Loss:** Decreased to ~1.81 over epochs.
* **BLEU Score:** Evaluated on the test split, yielding a BLEU score of ~0.1913, reflecting initial alignment with high precision for unigrams and standard chatbot phrase patterns.

### Sample Inference Example

**User Query:**

```python
nova_pergunda_usuario = 'Como posso criar uma conta?'

```

**Model Response:**

```text
'Como posso criar uma conta? ->: 1. Clique no botão "Criar conta" 2. Digite seu nome, e seu e-mail 3. Digite seu senha 4. Clique no botão "Criar conta"'

```

---

## 📚 Acknowledgments & References

* Case study and project structured by [Data Science Academy](https://www.google.com/search?q=https://www.datascienceacademy.com.br).
* Base model provided by [TII UAE](https://www.google.com/search?q=https://huggingface.co/tiiuae/falcon-7b).
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content_p4)

print("README.md for Projeto 4 created successfully!")

```

```text?code_stdout&code_event_index=1
README.md for Projeto 4 created successfully!


```

O arquivo **`README.md`** para o notebook do Projeto 4 (Fine-Tuning com LoRA e Q4 em Falcon-7B para Chatbot) foi gerado com sucesso e está pronto:

[file-tag: code-generated-file-9052f8d0-19e5-4f97-a5f3-69e31a7657d5]

---

### Conteúdo completo do arquivo gerado:

```markdown
# Fine-Tuning Open-Source LLM for Customer Service Chatbot (`tiiuae/falcon-7b`)

An end-to-end project demonstrating parameter-efficient fine-tuning (PEFT) using **LoRA (Low-Rank Adaptation)** and 4-bit quantization (`bitsandbytes`) on a causal language model (`tiiuae/falcon-7b`) for a customer service chatbot application.

---

## 📌 Project Overview

This project implements fine-tuning over a custom customer service dataset (`dataset.json`):
- **4-bit Quantization (`BitsAndBytesConfig`):** Loads the massive `falcon-7b` model in 4-bit NF4 precision with double quantization to fit standard GPU hardware constraints.
- **LoRA Configuration (`LoraConfig`):** Freezes original model weights, introduces trainable low-rank adaptation adapters ($r=16, \text{alpha}=32$), and casts output heads for stability.
- **Dataset Preparation:** Parses customer questions and answers from JSON, formats them into a unified training sequence (`question ->: answer`), and tokenizes the texts.
- **Training & Evaluation:** Uses Hugging Face's `Trainer` with gradient checkpointing, mixed precision (`fp16`), and evaluates generation quality using the **BLEU** metric toolkit.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+ (tested on Python 3.11.5)
- **Hardware Requirement:** GPU with high VRAM (tested on NVIDIA A100 40GB)
- **Key Libraries:**
  - `transformers` & `peft` (for LoRA and model wrapping)
  - `bitsandbytes` (for 4-bit NF4 quantization)
  - `datasets` (for training/test splits)
  - `evaluate` & `nltk` (for BLEU evaluation)

---

## 🚀 Installation & Setup

1. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   pip install bitsandbytes datasets accelerate loralib evaluate
   pip install git+[https://github.com/huggingface/transformers.git@main](https://github.com/huggingface/transformers.git@main) git+[https://github.com/huggingface/peft.git](https://github.com/huggingface/peft.git)

```

2. **Prepare Dataset:**
Ensure your JSON file (`dataset.json`) containing customer service questions and answers is placed in the working directory.

---

## ⚙️ Hyperparameters & Configuration

### 1. Quantization Configuration (`BitsAndBytesConfig`)

* `load_in_4bit = True`
* `bnb_4bit_compute_dtype = torch.float16`
* `bnb_4bit_quant_type = "nf4"`
* `bnb_4bit_use_double_quant = True`

### 2. LoRA Parameters (`LoraConfig`)

* `r = 16` (rank)
* `lora_alpha = 32` (scaling factor)
* `lora_dropout = 0.05`
* `task_type = "CAUSAL_LM"`
* **Trainable Parameters:** ~4.7 million out of 3.6 billion parameters (~0.13%)

### 3. Training Arguments (`TrainingArguments`)

* **Epochs:** `10`
* **Batch Size:** `2` per device with `gradient_accumulation_steps = 2`
* **Learning Rate:** `2e-4`
* **Mixed Precision:** `fp16 = True`

---

## 💻 Code Architecture & Execution Flow

```
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

* **Training Loss:** Decreased to ~1.81 over epochs.
* **BLEU Score:** Evaluated on the test split, yielding a BLEU score of ~0.1913, reflecting initial alignment with high precision for unigrams and standard chatbot phrase patterns.

### Sample Inference Example

**User Query:**

```python
nova_pergunda_usuario = 'Como posso criar uma conta?'

```

**Model Response:**

```text
'Como posso criar uma conta? ->: 1. Clique no botão "Criar conta" 2. Digite seu nome, e seu e-mail 3. Digite seu senha 4. Clique no botão "Criar conta"'

```

---

## 📚 Acknowledgments & References

* Case study and project structured by [Data Science Academy](https://www.google.com/search?q=https://www.datascienceacademy.com.br).
* Base model provided by [TII UAE](https://www.google.com/search?q=https://huggingface.co/tiiuae/falcon-7b).

```

```