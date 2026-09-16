# Fine-Tuning de LLM Open-Source para Aplicativo de Assistente (`google/flan-t5-base`)

Um projeto de aprendizado de máquina de ponta a ponta que demonstra o fine-tuning completo de um Grande Modelo de Linguagem codificador-decodificador (encoder-decoder) open-source (`google/flan-t5-base`) para aplicações de assistente de perguntas e respostas, utilizando o `Seq2SeqTrainer` do Hugging Face e métricas de avaliação `ROUGE`.

---

## 📌 Visão Geral do Projeto

Este projeto implementa fine-tuning supervisionado (SFT) sobre um conjunto de dados personalizado de Q&A (`dataset.csv`):
- **Divisão de Dados e Pré-processamento:** Carrega o conjunto de dados a partir de um CSV, realiza uma divisão de treino-teste de 80/20 (2.993 linhas de treino, 749 linhas de teste) e formata as entradas usando um prefixo de instrução (`"answer the question: "`).
- **Tokenização:** Tokeniza entradas e respostas alvo usando o `T5Tokenizer` com comprimentos adequados de preenchimento e truncamento (comprimento máximo de 128 para entradas, 512 para rótulos alvo).
- **Configuração de Treinamento:** Utiliza `Seq2SeqTrainingArguments` e `Seq2SeqTrainer` com um `DataCollatorForSeq2Seq` personalizado e avaliação por meio do kit de ferramentas de métricas **ROUGE** (`evaluate`).
- **Inferência e Persistência:** Salva os pesos do modelo treinado em disco (`modelo_salvo`) e os recarrega para geração de consultas personalizadas de assistente/jurídicas.

---

## 🛠️ Pilha Tecnológica e Requisitos

- **Linguagem:** Python 3.10+ (testado no Python 3.11.5)
- **Frameworks e Bibliotecas Principais:**
  - `transformers` (arquitetura codificador-decodificador T5)
  - `datasets` (para manipulação de datasets e divisões treino/teste)
  - `evaluate` & `rouge-score` (para validação do modelo)
  - `nltk` (para tokenização de sentenças nas métricas ROUGE)
  - `watermark` (para rastreamento de versão do ambiente)

---

## 🚀 Instalação e Configuração

1. **Instale os pacotes necessários:**
   ```bash
   pip install -r requirements.txt
   pip install watermark

```

2. **Prepare o Dataset:**
Certifique-se de que o seu arquivo de treinamento `dataset.csv` (contendo as colunas `question` e `answer`) esteja localizado no diretório de trabalho.

---

## ⚙️ Argumentos de Treinamento e Configuração

* **Modelo Base:** `google/flan-t5-base` (768 dimensões ocultas, 12 blocos encoder/decoder)
* **Épocas:** `3`
* **Tamanho do Lote (Batch Size):** `4` para treinamento, `2` para avaliação
* **Taxa de Aprendizado (Learning Rate):** `3e-4`
* **Weight Decay:** `0.01`
* **Otimizador / Agendador:** Padrões do Seq2Seq trainer com geração de sequências ativada durante a avaliação (`predict_with_generate=True`).

---

## 📊 Resultados de Treinamento e Métricas de Avaliação

Avaliado ao longo de 3 épocas usando o pacote de métricas **ROUGE** na divisão de teste (749 amostras):

| Época | Perda de Treino (Training Loss) | Perda de Validação (Validation Loss) | Rouge1 | Rouge2 | Rougel | Rougelsum |
| --- | --- | --- | --- | --- | --- | --- |
| **1** | 2,7419 | 2,4528 | 0,1277 | 0,0292 | 0,1028 | 0,1029 |
| **2** | 2,2523 | 2,4221 | 0,1295 | 0,0312 | 0,1055 | 0,1055 |
| **3** | 2,7139 | 2,4159 | 0,1299 | 0,0302 | 0,1049 | 0,1050 |

*(Tempo total de treinamento: ~17 minutos em GPU)*

---

## 💻 Exemplo de Inferência e Uso

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Carregar o modelo com fine-tuning e o tokenizador do disco
tokenizer = AutoTokenizer.from_pretrained('modelo_salvo')
model = AutoModelForSeq2SeqLM.from_pretrained('modelo_salvo')

# Prompt de Entrada
query = "Can I move out of state with my children if I have a custody agreement in that state?"
input_ids = tokenizer(query, return_tensors="pt").input_ids

# Gerar Resposta
outputs = model.generate(input_ids, max_length=50, temperature=0.4, do_sample=True)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Pergunta:", query)
print("Resposta:", response)

```

---

## 📚 Agradecimentos e Referências

* Estudo de caso e projeto estruturado pela [Data Science Academy](https://www.datascienceacademy.com.br).
* Modelo pré-treinado fornecido pelo Google via [Hugging Face (`google/flan-t5-base`)](https://huggingface.co/google/flan-t5-base).




<br>
<br>

---

<br>
<br>

## English
<br>

# Fine-Tuning Open-Source LLM for Assistant App (`google/flan-t5-base`)

An end-to-end machine learning project demonstrating full fine-tuning of an open-source encoder-decoder Large Language Model (`google/flan-t5-base`) for question-answering assistant applications using Hugging Face's `Seq2SeqTrainer` and `ROUGE` evaluation metrics.

---

## 📌 Project Overview

This project implements supervised fine-tuning (SFT) over a custom Q&A dataset (`dataset.csv`):
- **Data Split & Preprocessing:** Loads dataset from CSV, performs an 80/20 train-test split (2,993 training rows, 749 test rows), and formats inputs using a instruction prefix (`"answer the question: "`).
- **Tokenization:** Tokenizes inputs and target answers using `T5Tokenizer` with appropriate padding/truncation lengths (max length 128 for inputs, 512 for target labels).
- **Training Setup:** Uses `Seq2SeqTrainingArguments` and `Seq2SeqTrainer` with a custom `DataCollatorForSeq2Seq` and evaluation via the **ROUGE** metric toolkit (`evaluate`).
- **Inference & Persistence:** Saves the trained model weights to disk (`modelo_salvo`) and reloads them for custom legal/assistant query generation.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+ (tested on Python 3.11.5)
- **Frameworks & Key Libraries:**
  - `transformers` (T5 encoder-decoder architecture)
  - `datasets` (for dataset handling & train/test splits)
  - `evaluate` & `rouge-score` (for model validation)
  - `nltk` (for sentence tokenization in ROUGE metrics)
  - `watermark` (for environment version tracking)

---

## 🚀 Installation & Setup

1. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   pip install watermark
   ```

2. **Prepare Dataset:**
   Ensure your training file `dataset.csv` (containing `question` and `answer` columns) is located in the working directory.

---

## ⚙️ Training Arguments & Configuration

- **Base Model:** `google/flan-t5-base` (768 hidden dimensions, 12 encoder/decoder blocks)
- **Epochs:** `3`
- **Batch Size:** `4` for training, `2` for evaluation
- **Learning Rate:** `3e-4`
- **Weight Decay:** `0.01`
- **Optimizer / Scheduler:** Standard Seq2Seq trainer defaults with sequence generation enabled during evaluation (`predict_with_generate=True`).

---

## 📊 Training Results & Evaluation Metrics

Evaluated across 3 epochs using the **ROUGE** metrics suite on the test split (749 samples):

| Epoch | Training Loss | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 2.7419 | 2.4528 | 0.1277 | 0.0292 | 0.1028 | 0.1029 |
| **2** | 2.2523 | 2.4221 | 0.1295 | 0.0312 | 0.1055 | 0.1055 |
| **3** | 2.7139 | 2.4159 | 0.1299 | 0.0302 | 0.1049 | 0.1050 |

*(Total training time: ~17 minutes on GPU)*

---

## 💻 Inference & Usage Example

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load fine-tuned model and tokenizer from disk
tokenizer = AutoTokenizer.from_pretrained('modelo_salvo')
model = AutoModelForSeq2SeqLM.from_pretrained('modelo_salvo')

# Input Prompt
query = "Can I move out of state with my children if I have a custody agreement in that state?"
input_ids = tokenizer(query, return_tensors="pt").input_ids

# Generate Response
outputs = model.generate(input_ids, max_length=50, temperature=0.4, do_sample=True)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Question:", query)
print("Answer:", response)
```

---

## 📚 Acknowledgments & References
- Pretrained model provided by Google via [Hugging Face (`google/flan-t5-base`)](https://huggingface.co/google/flan-t5-base).
