# Text Generation with GPT-2 Large in Python

A hands-on case study demonstrating how to load a pre-trained Large Language Model (LLM) using Hugging Face's `transformers` and generate coherent text using Beam Search.

---

## 📌 Project Overview

This project showcases the end-to-end pipeline of text generation with a pre-trained **GPT-2 Large** model. It covers:
- Loading pre-trained weights and tokenizers from the Hugging Face Hub.
- Converting natural language prompts into numeric PyTorch tensors via BPE tokenization.
- Fine-tuning text generation parameters (Beam Search, n-gram penalties, max token length, early stopping).
- Decoding generated token IDs back into human-readable text.

---

## 🛠️ Tech Stack & Requirements

- **Python**: 3.10+ (tested on 3.11.5)
- **PyTorch**: Required backend for PyTorch tensor generation (`return_tensors='pt'`)
- **TensorFlow**: `2.14.0`
- **Hugging Face Transformers**: `4.35.2`
- **Watermark**: For environment and dependency tracking

---

## 🚀 Installation & Setup

You can install all required packages using `pip`:

```bash
pip install watermark
pip install tensorflow==2.14.0
pip install transformers==4.35.2
pip install torch
```

> **Note:** A GPU environment (such as Google Colab with standard T4/V100 GPU) is recommended, as `gpt2-large` is approximately ~3.25 GB in size (774M parameters).

---

## 🧠 Model Architecture & Concepts

### 1. Tokenizer (`GPT2Tokenizer`)
- Model identifier: `gpt2-large`
- Vocabulary size: `50,257`
- Context window: `1,024` tokens
- Encodes input text into token IDs (`tensor([[ 2061, 318, 35941, 9345]])` for `"What is Artificial Intelligence"`).

### 2. Language Model (`GPT2LMHeadModel`)
- GPT-2 model with a causal language modeling head (`lm_head: Linear(1280 -> 50257)`).
- 36 transformer layers (`GPT2Block`), hidden size of 1280, 20 attention heads.
- Padding token aligned to End-Of-Sequence token (`pad_token_id = tokenizer.eos_token_id`).

---

## 💻 Code Example / Usage

```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 1. Load Tokenizer and Pretrained Model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
model = GPT2LMHeadModel.from_pretrained("gpt2-large", pad_token_id=tokenizer.eos_token_id)

# 2. Prepare Input Prompt
prompt = "What is Artificial Intelligence"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# 3. Generate Text with Beam Search
output_ids = model.generate(
    input_ids,
    max_length=100,
    num_beams=5,
    no_repeat_ngram_size=2,
    early_stopping=True
)

# 4. Decode the Output Tokens
generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(generated_text)
```

### Generation Hyperparameters Explained
| Parameter | Value | Purpose |
| :--- | :--- | :--- |
| `max_length` | `100` | Maximum combined length (prompt + completion) in tokens. |
| `num_beams` | `5` | Uses Beam Search with 5 beams to explore top-probability word sequences instead of greedy selection. |
| `no_repeat_ngram_size` | `2` | Prevents the model from repeating 2-word combinations, minimizing repetitive text. |
| `early_stopping` | `True` | Stops generation as soon as all beam candidates reach the end-of-sequence (`eos_token`). |

---

## 📄 Example Output

**Input Prompt:**
```
What is Artificial Intelligence
```

**Model Output:**
```text
What is Artificial Intelligence?

Artificial intelligence (AI) is a branch of computer science that deals with computer programs 
that are able to learn and adapt to their environment. AI has been around for a long time, 
but it is only recently that computers have become capable of performing tasks that were 
once thought to be beyond the capabilities of human beings. For example, a computer program 
can learn how to play a video game by playing the same game over and over again. This is called 
reinforcement learning.
```

---

## 📚 Acknowledgments & References
- Course / Case Study originally inspired by [Data Science Academy](https://www.datascienceacademy.com.br).
- Pretrained weights hosted on [Hugging Face Models (gpt2-large)](https://huggingface.co/gpt2-large).
