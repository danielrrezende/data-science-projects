# Custom Data Fine-Tuning & Web Deployment of GPT-2 for Arithmetic Reasoning

An end-to-end tutorial project demonstrating how to train a miniature Language Model (based on GPT-2 architecture) from scratch to perform single-digit addition, showcasing tokenization, fine-tuning, reasoning concepts, and deployment via Gradio.

---

## 📌 Project Overview

This project is divided into two distinct phases: **Training** and **Deployment**. 

### 1. Training Phase (`Projeto8-Treinamento.ipynb`)
- **Custom Architecture:** Configures a heavily downsized GPT-2 architecture (`n_layer=2`, `n_head=4`) with ~15 million parameters specifically optimized for a tiny context window.
- **Custom Tokenizer:** Builds a bespoke Python tokenizer (`DSATokenizer`) mapped strictly to a vocabulary of 13 tokens (`0-9`, `+`, `=`, and a padding token `-1`).
- **Data Engineering:** Generates a synthetic dataset of 1,000,000 single-digit addition equations formatted as sequences (e.g., `2 + 3 = 0 5`) and wraps it in a PyTorch `Dataset`.
- **Model Training:** Utilizes Hugging Face `Accelerate` to train the model from scratch over 2 epochs using standard cross-entropy loss, teaching the LLM the logical "reasoning" of addition.
- **Evaluation:** Evaluates the model's accuracy directly against synthetic math problems to guarantee convergence.

### 2. Deployment Phase (`Projeto8-Deploy.ipynb`)
- **Model Loading:** Loads the newly trained weights (`llm_dsa_final`) alongside the custom tokenizer logic.
- **Inference Pipeline:** Implements an autoregressive prediction loop (`dsa_faz_previsao`) that continually extracts the highest-probability logit.
- **Web UI:** Wraps the entire inference engine inside a highly accessible **Gradio** web application (`gr.Interface`), allowing users to input math strings interactively (e.g., `5 + 3 =`) and receive LLM-generated results in real-time.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+
- **Deep Learning Framework:** PyTorch (`torch==2.3.0`)
- **Training Orchestration:** `transformers==4.40.1`, `accelerate==0.29.3`
- **Web Deployment Framework:** `gradio==4.31.5`
- **Other:** `numpy`

---

## 🚀 Installation & Setup

```bash
# 1. Clone repository & install dependencies
pip install torch==2.3.0 transformers==4.40.1 accelerate==0.29.3 gradio==4.31.5 watermark

# 2. Run the Training Notebook
# Execute 'Projeto8-Treinamento.ipynb' to train the model from scratch. 
# This will output a trained model directory named "llm/llm_dsa_final".

# 3. Run the Deployment Notebook
# Execute 'Projeto8-Deploy.ipynb' to load the trained model and launch the Gradio web interface.

```

---

## ⚙️ Architecture & Model Configurations

### LLM Specifications

* Base Architecture: `GPT2LMHeadModel`
* Vocabulary Size: `13`
* Context Length: `6` tokens
* Layers: `2`
* Attention Heads: `4`
* Total Parameters: `15.0M`

### Training Hyperparameters

* Epochs: `2`
* Batch Size: `100`
* Optimizer: `Adam`
* Loss Function: `CrossEntropyLoss` (ignoring pad token)

---

## 💻 Gradio Web Interface Usage

Once the deployment script is running, open the generated local URL (or public Gradio share link).

1. **Input:** Type a single-digit addition problem in the exact format it was trained on, including spaces. For example: `4 + 5 =`
2. **Output:** The LLM will autoregressively predict the outcome in a two-digit format. Result: `0 9`

---

## 📚 Acknowledgments & References

* Coursework and architectural design inspired by [Data Science Academy](https://www.datascienceacademy.com.br).
* Neural network framework powered by [PyTorch](https://pytorch.org/).
* Transformers architecture powered by [Hugging Face](https://huggingface.co/).
* Frontend UI generation powered by [Gradio](https://www.gradio.app/).
