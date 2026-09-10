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
- Case study and project structured by [Data Science Academy](https://www.datascienceacademy.com.br).
- Pretrained model provided by Google via [Hugging Face (`google/flan-t5-base`)](https://huggingface.co/google/flan-t5-base).
