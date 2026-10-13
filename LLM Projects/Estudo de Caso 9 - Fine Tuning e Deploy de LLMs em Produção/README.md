## 📌 Visão Geral do Projeto

Este projeto é dividido em duas fases distintas: **Treinamento** e **Deploy**. 

### 1. Fase de Treinamento (`Projeto8-Treinamento.ipynb`)
- **Arquitetura Customizada:** Configura uma arquitetura GPT-2 fortemente reduzida (`n_layer=2`, `n_head=4`) com ~15 milhões de parâmetros, otimizada especificamente para uma janela de contexto minúscula.
- **Tokenizador Customizado:** Constrói um tokenizador Python sob medida (`DSATokenizer`) mapeado estritamente para um vocabulário de 13 tokens (`0-9`, `+`, `=`, e um token de preenchimento/padding `-1`).
- **Engenharia de Dados:** Gera um conjunto de dados sintético de 1.000.000 de equações de adição de um único dígito formatadas como sequências (ex: `2 + 3 = 0 5`) e as encapsula em um `Dataset` do PyTorch.
- **Treinamento do Modelo:** Utiliza o `Accelerate` da Hugging Face para treinar o modelo do zero ao longo de 2 épocas (epochs) usando a função de perda de entropia cruzada padrão (cross-entropy loss), ensinando ao LLM o "raciocínio" lógico da adição.
- **Avaliação:** Avalia a precisão (accuracy) do modelo diretamente com problemas matemáticos sintéticos para garantir a convergência.

### 2. Fase de Deploy (`Projeto8-Deploy.ipynb`)
- **Carregamento do Modelo:** Carrega os pesos recém-treinados (`llm_dsa_final`) junto com a lógica do tokenizador customizado.
- **Pipeline de Inferência:** Implementa um loop de previsão autorregressivo (`dsa_faz_previsao`) que extrai continuamente o logit de maior probabilidade.
- **Interface Web:** Encapsula todo o mecanismo de inferência dentro de uma aplicação web **Gradio** altamente acessível (`gr.Interface`), permitindo que os usuários insiram strings matemáticas de forma interativa (ex: `5 + 3 =`) e recebam os resultados gerados pelo LLM em tempo real.

---

## 🛠️ Stack Tecnológico e Requisitos

- **Linguagem:** Python 3.10+
- **Framework de Deep Learning:** PyTorch (`torch==2.3.0`)[cite: 26, 27]
- **Orquestração de Treinamento:** `transformers==4.40.1`, `accelerate==0.29.3`[cite: 26, 27]
- **Framework de Deploy Web:** `gradio==4.31.5`[cite: 27]
- **Outros:** `numpy`, `watermark`[cite: 26, 27]

---

## 🚀 Instalação e Configuração

```bash
# 1. Clone o repositório e instale as dependências
pip install torch==2.3.0 transformers==4.40.1 accelerate==0.29.3 gradio==4.31.5 watermark

# 2. Execute o Notebook de Treinamento
# Execute 'Projeto8-Treinamento.ipynb' para treinar o modelo do zero. 
# Isso gerará um diretório com o modelo treinado chamado "llm/llm_dsa_final".

# 3. Execute o Notebook de Deploy
# Execute 'Projeto8-Deploy.ipynb' para carregar o modelo treinado e iniciar a interface web do Gradio.

```

---

## ⚙️ Arquitetura e Configurações do Modelo

### Especificações do LLM

* Arquitetura Base: `GPT2LMHeadModel`

* Tamanho do Vocabulário: `13`

* Comprimento do Contexto: `6` tokens


* Camadas (Layers): `2`

* Cabeças de Atenção (Attention Heads): `4`

* Total de Parâmetros: `15.0M`


### Hiperparâmetros de Treinamento

* Épocas (Epochs): `2`

* Tamanho do Lote (Batch Size): `100`

* Otimizador: `Adam`

* Função de Perda (Loss): `CrossEntropyLoss` (ignorando o token de padding)



---

## 💻 Uso da Interface Web Gradio

Assim que o script de deploy estiver em execução, abra a URL local gerada (ou o link público compartilhado do Gradio).

1. **Input (Entrada):** Digite um problema de adição de um único dígito no formato exato em que o modelo foi treinado, incluindo os espaços. Por exemplo: `4 + 5 =`

2. **Output (Saída):** O LLM fará a previsão autorregressiva do resultado em um formato de dois dígitos. Resultado: `0 9`


---

## 📚 Agradecimentos e Referências

* Framework de rede neural desenvolvido com [PyTorch](https://pytorch.org/).
* Arquitetura Transformers baseada na [Hugging Face](https://huggingface.co/gpt2).


* Geração da interface de usuário em frontend através do [Gradio](https://www.gradio.app/).



<br>
<br>

---

<br>
<br>

## English
<br>

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

* Neural network framework powered by [PyTorch](https://pytorch.org/).
* Transformers architecture powered by [Hugging Face](https://huggingface.co/).
* Frontend UI generation powered by [Gradio](https://www.gradio.app/).
