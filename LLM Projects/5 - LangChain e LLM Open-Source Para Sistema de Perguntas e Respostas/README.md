# Instruction Fine-Tuning & LangChain QA System with Open-Source LLM (`Llama-2-7b-chat-hf`)

An end-to-end implementation of parameter-efficient instruction fine-tuning using **QLoRA** on `Llama-2-7b-chat-hf`, followed by the integration of the fine-tuned model into a conversational Question & Answering pipeline powered by **LangChain**.

---

## 📌 Project Overview

This project builds a specialized domain-specific Question & Answering assistant using the `nlpie/Llama2-MedTuned-Instructions` dataset:
- **Instruction Data Preprocessing:** Prepares supervised fine-tuning prompts by wrapping instruction, input context, and expected output into the standard LLaMA-2 chat formatting template (`[INST]<<SYS>>...[/INST]`).
- **4-Bit QLoRA Fine-Tuning:** Loads the base model in 4-bit NormalFloat (`nf4`) via `bitsandbytes`, attaches low-rank adapters (`r=8, alpha=16`) with `peft`, and executes instruction tuning via TRL's `SFTTrainer`.
- **Adapter Merging:** Merges trained LoRA adapters back into the base model weights with `merge_and_unload()` for optimized deployment and single-model inference.
- **LangChain Pipeline & Memory:** Wraps the merged model in a `HuggingFacePipeline`, establishes a prompt template with `PromptTemplate`, and equips the model with stateful interaction using `ConversationBufferMemory` in an `LLMChain`.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+ (tested on Python 3.11.5)
- **Hardware Requirement:** GPU with CUDA support (tested on NVIDIA A100 40GB)
- **Frameworks & Key Libraries:**
  - `transformers` & `peft`
  - `bitsandbytes` & `accelerate`
  - `trl` (for `SFTTrainer`)
  - `datasets` (Hugging Face Datasets)
  - `langchain` & `langchain-community`
  - `watermark`

---

## 🚀 Installation & Setup

1. **Install required libraries:**
   ```bash
   pip install -q accelerate peft bitsandbytes transformers trl datasets langchain watermark
   ```

2. **Dataset:**
   The notebook pulls directly from the Hugging Face Hub:
   - Dataset: [`nlpie/Llama2-MedTuned-Instructions`](https://huggingface.co/datasets/nlpie/Llama2-MedTuned-Instructions)
   - Base Model: [`NousResearch/Llama-2-7b-chat-hf`](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf)

---

## ⚙️ Hyperparameters & Configuration

### 1. Quantization (`BitsAndBytesConfig`)
- `load_in_4bit = True`
- `bnb_4bit_compute_dtype = "float16"`
- `bnb_4bit_quant_type = "nf4"`
- `use_nested_quant = False`

### 2. LoRA Settings (`LoraConfig`)
- `r = 8`
- `lora_alpha = 16`
- `lora_dropout = 0.05`
- `bias = "none"`
- `task_type = "CAUSAL_LM"`

### 3. SFT Training Arguments (`TrainingArguments`)
- **Optimizer:** `paged_adamw_32bit`
- **Learning Rate:** `2e-4` (cosine scheduler)
- **Batch Size:** `1` per device with `gradient_accumulation_steps = 4`
- **Training Steps:** `150` max steps with `fp16 = True`
- **Sequence Length:** `max_seq_length = 512` with sequence packing enabled (`packing = True`)

---

## 💻 Architecture & Workflow

```
[ nlpie/Llama2-MedTuned-Instructions ]
                  │
                  ▼
[ Custom Prompt Template Formatting ] ──► TRL SFTTrainer
                  │                              │
[ Llama-2-7b-chat-hf (4-bit QLoRA) ] ────────────┘
                  │
                  ▼
       [ 150 Training Steps ]
                  │
                  ▼
       [ Save & Merge LoRA Adapter ]
                  │
                  ▼
   [ Hugging Face Pipeline ] (text-generation)
                  │
                  ▼
   [ LangChain LLMChain + ConversationBufferMemory ]
                  │
                  ▼
     [ Interactive QA Assistant ]
```

---

## 💬 Sample Query & Output

**User Question (Context):**
```text
###Question: All of the following provisions are included in the Primary health care according to the Alma Ata declaration except:
###Options:
A. Adequate supply of safe drinking water
B. Nutrition
C. Provision of free medicines
D. Basic sanitation
```

**Assistant Response:**
```text
Great! Let's analyze the question and answer options:

Question: All of the following provisions are included in the Primary health care according to the Alma Ata declaration except:

Options:
A. Adequate supply of safe drinking water
B. Nutrition
C. Provision of free medicines
D. Basic sanitation

The Alma Ata declaration is a widely recognized international document that outlines the principles of primary health care. According to the declaration, primary health care should include the following provisions:

* Adequate supply of safe drinking water
* Nutrition
* Provision of free medicines
* Basic sanitation

However, the question asks about the exception, which is not included in the Alma Ata declaration. Therefore, the best answer is (D) Basic sanitation.
```

---

## 📚 Acknowledgments & References
- Project developed as part of coursework at [Data Science Academy](https://www.datascienceacademy.com.br).
- Pretrained model hosted by [NousResearch / Hugging Face](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf).
- Dataset curated by [nlpie on Hugging Face](https://huggingface.co/datasets/nlpie/Llama2-MedTuned-Instructions).
