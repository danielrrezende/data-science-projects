# Fine-Tuning de LLM Open-Source para Aplicativo de Assistente (`google/flan-t5-base`)

Um projeto de aprendizado de máquina de ponta a ponta que demonstra o fine-tuning completo de um Grande Modelo de Linguagem codificador-decodificador (encoder-decoder) open-source (`google/flan-t5-base`) para aplicações de assistente de perguntas e respostas, utilizando o `Seq2SeqTrainer` do Hugging Face e métricas de avaliação `ROUGE`[cite: 2].

---

## 📌 Visão Geral do Projeto

Este projeto implementa fine-tuning supervisionado (SFT) sobre um conjunto de dados personalizado de Q&A (`dataset.csv`):
- **Divisão de Dados e Pré-processamento:** Carrega o conjunto de dados a partir de um CSV, realiza uma divisão de treino-teste de 80/20 (2.993 linhas de treino, 749 linhas de teste) e formata as entradas usando um prefixo de instrução (`"answer the question: "`)[cite: 2].
- **Tokenização:** Tokeniza entradas e respostas alvo usando o `T5Tokenizer` (carregado a partir de `google/flan-t5-small`) com comprimentos adequados de preenchimento e truncamento (comprimento máximo de 128 para entradas, 512 para rótulos alvo)[cite: 2].
- **Configuração de Treinamento:** Utiliza `Seq2SeqTrainingArguments` e `Seq2SeqTrainer` com um `DataCollatorForSeq2Seq` personalizado e avaliação por meio do kit de ferramentas de métricas **ROUGE** (`evaluate`)[cite: 2].
- **Inferência e Persistência:** Salva os pesos do modelo treinado em disco (`modelo_salvo`) e os recarrega para geração de consultas personalizadas de assistente/jurídicas[cite: 2].

---

## 🛠️ Pilha Tecnológica e Requisitos

- **Linguagem:** Python 3.12.13[cite: 2]
- **Frameworks e Bibliotecas Principais:**
  - `transformers` v4.41.2 (arquitetura codificador-decodificador T5)[cite: 2]
  - `datasets` v2.20.0 (para manipulação de datasets e divisões treino/teste)[cite: 2]
  - `evaluate` v0.4.2 & `rouge-score` v0.1.2 (para validação do modelo)[cite: 2]
  - `nltk` v3.8.1 (para tokenização de sentenças nas métricas ROUGE)[cite: 2]
  - `torch` v2.3.1 e dependências auxiliares como `fsspec` v2024.5.0 e `accelerate` v0.31.0[cite: 2]

---

## 🚀 Instalação e Configuração

1. **Instale os pacotes necessários configurando as versões exatas para estabilidade:**
   ```bash
   pip uninstall -y numpy scipy torchaudio torchvision textblob ydata-profiling peft
   pip install -q 'numpy<2.1' 'scipy<1.15'
   pip install -q fsspec==2024.5.0
   pip install -q torch==2.3.1 transformers==4.41.2 tokenizers==0.19.1 datasets==2.20.0 evaluate==0.4.2 rouge_score==0.1.2 sentencepiece==0.2.0 accelerate==0.31.0 nltk==3.8.1
   ```[cite: 2]

2. **Prepare o Dataset:**
Certifique-se de que o seu arquivo de treinamento `dataset.csv` (contendo as colunas `question` e `answer`) esteja localizado no diretório correspondente[cite: 2].

---

## ⚙️ Argumentos de Treinamento e Configuração

* **Modelo Base:** `google/flan-t5-base` (768 dimensões ocultas, 12 blocos encoder/decoder)[cite: 2]
* **Épocas:** `3`[cite: 2]
* **Tamanho do Lote (Batch Size):** `4` para treinamento, `2` para avaliação[cite: 2]
* **Taxa de Aprendizado (Learning Rate):** `3e-4`[cite: 2]
* **Weight Decay:** `0.01`[cite: 2]
* **Otimizador / Agendador:** Padrões do Seq2Seq trainer com geração de sequências ativada durante a avaliação (`predict_with_generate=True`)[cite: 2].

---

## 📊 Resultados de Treinamento e Métricas de Avaliação

Avaliado ao longo de 3 épocas usando o pacote de métricas **ROUGE** na divisão de teste (749 amostras)[cite: 2]:

| Época | Perda de Treino (Training Loss) | Perda de Validação (Validation Loss) | Rouge1 | Rouge2 | Rougel | Rougelsum |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 2.6112 | 2.4173 | 0.1231 | 0.0288 | 0.0992 | 0.0992 |
| **2** | 2.3192 | 2.3721 | 0.1217 | 0.0281 | 0.0989 | 0.0989 |
| **3** | 1.9859 | 2.3664 | 0.1221 | 0.0296 | 0.0989 | 0.0988 |

*(Tempo total de treinamento: ~27 minutos e 30 segundos em GPU)*[cite: 2]

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

```[cite: 2]

**Saída Gerada:**
```text
Pergunta: Can I move out of state with my children if I have a custody agreement in that state?
Resposta: The custody agreement in your state will be binding. If you are planning to move out of state, you will need to file a motion for a divorce. If you are unable to get a divorce, you may have grounds to
```[cite: 2]

---

## 📚 Agradecimentos e Referências

* Modelo pré-treinado fornecido pelo Google via [Hugging Face (`google/flan-t5-base`)](https://huggingface.co/google/flan-t5-base)[cite: 2].


<br>
<br>

---

<br>
<br>

## English
<br>

# Fine-Tuning Open-Source LLM for Assistant App (`google/flan-t5-base`)

An end-to-end machine learning project demonstrating full fine-tuning of an open-source encoder-decoder Large Language Model (`google/flan-t5-base`) for question-answering assistant applications using Hugging Face's `Seq2SeqTrainer` and `ROUGE` evaluation metrics[cite: 2].

---

## 📌 Project Overview

This project implements supervised fine-tuning (SFT) over a custom Q&A dataset (`dataset.csv`):
- **Data Split & Preprocessing:** Loads dataset from CSV, performs an 80/20 train-test split (2,993 training rows, 749 test rows), and formats inputs using a instruction prefix (`"answer the question: "`)[cite: 2].
- **Tokenization:** Tokenizes inputs and target answers using `T5Tokenizer` (loaded via `google/flan-t5-small`) with appropriate padding/truncation lengths (max length 128 for inputs, 512 for target labels)[cite: 2].
- **Training Setup:** Uses `Seq2SeqTrainingArguments` and `Seq2SeqTrainer` with a custom `DataCollatorForSeq2Seq` and evaluation via the **ROUGE** metric toolkit (`evaluate`)[cite: 2].
- **Inference & Persistence:** Saves the trained model weights to disk (`modelo_salvo`) and reloads them for custom legal/assistant query generation[cite: 2].

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.12.13[cite: 2]
- **Frameworks & Key Libraries:**
  - `transformers` v4.41.2 (T5 encoder-decoder architecture)[cite: 2]
  - `datasets` v2.20.0 (for dataset handling & train/test splits)[cite: 2]
  - `evaluate` v0.4.2 & `rouge-score` v0.1.2 (for model validation)[cite: 2]
  - `nltk` v3.8.1 (for sentence tokenization in ROUGE metrics)[cite: 2]
  - `torch` v2.3.1 along with `fsspec` v2024.5.0 and `accelerate` v0.31.0[cite: 2]

---

## 🚀 Installation & Setup

1. **Install required packages using strict versioning for stability:**
   ```bash
   pip uninstall -y numpy scipy torchaudio torchvision textblob ydata-profiling peft
   pip install -q 'numpy<2.1' 'scipy<1.15'
   pip install -q fsspec==2024.5.0
   pip install -q torch==2.3.1 transformers==4.41.2 tokenizers==0.19.1 datasets==2.20.0 evaluate==0.4.2 rouge_score==0.1.2 sentencepiece==0.2.0 accelerate==0.31.0 nltk==3.8.1
   ```[cite: 2]

2. **Prepare Dataset:**
   Ensure your training file `dataset.csv` (containing `question` and `answer` columns) is located in the working directory[cite: 2].

---

## ⚙️ Training Arguments & Configuration

- **Base Model:** `google/flan-t5-base` (768 hidden dimensions, 12 encoder/decoder blocks)[cite: 2]
- **Epochs:** `3`[cite: 2]
- **Batch Size:** `4` for training, `2` for evaluation[cite: 2]
- **Learning Rate:** `3e-4`[cite: 2]
- **Weight Decay:** `0.01`[cite: 2]
- **Optimizer / Scheduler:** Standard Seq2Seq trainer defaults with sequence generation enabled during evaluation (`predict_with_generate=True`)[cite: 2].

---

## 📊 Training Results & Evaluation Metrics

Evaluated across 3 epochs using the **ROUGE** metrics suite on the test split (749 samples)[cite: 2]:

| Epoch | Training Loss | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 2.6112 | 2.4173 | 0.1231 | 0.0288 | 0.0992 | 0.0992 |
| **2** | 2.3192 | 2.3721 | 0.1217 | 0.0281 | 0.0989 | 0.0989 |
| **3** | 1.9859 | 2.3664 | 0.1221 | 0.0296 | 0.0989 | 0.0988 |

*(Total training time: ~27 minutes and 30 seconds on GPU)*[cite: 2]

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
```[cite: 2]

**Generated Output:**
```text
Question: Can I move out of state with my children if I have a custody agreement in that state?
Answer: The custody agreement in your state will be binding. If you are planning to move out of state, you will need to file a motion for a divorce. If you are unable to get a divorce, you may have grounds to
```[cite: 2]

---

## 📚 Acknowledgments & References
- Pretrained model provided by Google via [Hugging Face (`google/flan-t5-base`)](https://huggingface.co/google/flan-t5-base)[cite: 2].