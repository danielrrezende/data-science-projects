<a id="top"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

---

<a id="pt-br"></a>

# 🇧🇷 Manutenção Preditiva de Ativos - Paper CO

Este projeto tem como objetivo apoiar a tomada de decisão em manutenção preditiva para ativos industriais, com foco em prever falhas antes que elas ocorram e reduzir custos operacionais. A ideia principal é avaliar a viabilidade de um modelo de predição de falha e, idealmente, estimar o tempo restante de vida útil (RUL) dos ativos com horizonte de previsão de pelo menos 20 ciclos.

O cenário do caso é inspirado em uma operação de produção de celulose e papel, em que a manutenção programada por calendário pode levar a inspeções excessivas, gastos desnecessários e, ao mesmo tempo, não evitar falhas inesperadas em equipamentos críticos.

---

## 🎯 Objetivo do Projeto

A Paper CO precisa reduzir custos de manutenção sem comprometer a disponibilidade de seus ativos. Para isso, o desafio é responder três perguntas centrais:

* É possível prever falhas com antecedência suficiente para agir antes da quebra?
* Qual é o melhor indicador para a decisão de manutenção: risco de falha, probabilidade de falha em 20 ciclos ou vida útil restante (RUL)?
* Como esse modelo pode substituir ou complementar uma política de troca por tempo fixo?

---

## 📌 Contexto de Negócio

A indústria de celulose e papel opera em um ambiente competitivo, com pressão sobre margens e custos. Manutenções excessivas aumentam custos sem agregar valor, enquanto manutenção tardia pode resultar em paradas não planejadas, perda de produção e risco de segurança.

Nesse contexto, a manutenção preditiva se torna uma estratégia estratégica: usar dados operacionais e de sensores para detectar degradação e planejar intervenções no momento certo.

---

## 🧠 Entregáveis Esperados

O projeto busca produzir:

* análise exploratória dos dados dos ativos;
* identificação de padrões e sinais de degradação;
* modelagem preditiva para falha ou RUL;
* avaliação quantitativa do desempenho do modelo;
* comparação com uma política ingênua de manutenção por tempo fixo;
* recomendações para uso prático pelos times de manutenção e operação.

---

## 🗂️ Estrutura do Repositório

```text
.
├── dataset/
│   ├── PM_train.txt          # Dados de treinamento
│   ├── PM_test.txt           # Dados de teste
│   └── ...
├── anotacoes.py              # Notas do caso e contexto técnico
├── exemplo_submissao.csv     # Exemplo de formato de saída
├── note-suzano.ipynb         # Notebook principal de exploração e modelagem
├── note-feat-imp.ipynb       # Experimentos complementares de importância de variáveis
├── Case Manutenção Preditiva.zip
├── Complete Case Pulp and Paper - Predictive Maintanance.docx
├── Complete Case Pulp and Paper - Predictive Maintanance_pt.docx
└── README.md
```

---

## 📊 Dicionário dos Dados

Os dados de treinamento e teste contêm informações por ciclo de operação para cada ativo. A estrutura geral inclui:

| Campo | Descrição |
| :--- | :--- |
| `id_recurso` | Identificador do ativo. Cada sequência representa uma vida útil completa do equipamento até a falha. |
| `tmp_exe` | Tempo de operação / contador do ciclo de execução. |
| `cfg1`, `cfg2`, `cfg3` | Configurações operacionais do ativo. |
| `tag1` a `tag21` | Medidas de sensores ou indicadores físicos associados ao desempenho do equipamento. |

A base de dados está em formato separado por espaço, sem cabeçalho explícito, e é tratada como uma tabela de séries temporais por ativo em regime de operação.

---

## 🔍 Fluxo de Trabalho do Projeto

1. Leitura e limpeza dos dados de treinamento.
2. Análise exploratória de distribuições e padrões de falha.
3. Extração de sinais relevantes por ativo e por ciclo.
4. Construção de um alvo supervisionado (falha em 20 ciclos ou RUL).
5. Treinamento de modelos de machine learning.
6. Validação com métricas de classificação/regressão relevantes.
7. Comparação do modelo com manutenção fixa por calendário.
8. Geração do arquivo final para submissão e apresentação.

---

## 🧪 Tecnologias e Ferramentas

As análises foram desenvolvidas em um stack Python típico para ciência de dados e manutenção preditiva:

* Python 3
* NumPy
* pandas
* scikit-learn
* matplotlib
* seaborn
* Jupyter Notebook

---

## ⚙️ Pré-requisitos

Para reproduzir a análise localmente, recomenda-se:

```bash
python --version
```

Em seguida, instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install jupyter pandas numpy scikit-learn matplotlib seaborn
```

---

## ▶️ Como Executar

### 1. Abrir o ambiente de análise

```bash
jupyter notebook
```

Ou, se preferir:

```bash
jupyter lab
```

### 2. Carregar os dados

Os arquivos principais estão em `dataset/`:

```text
dataset/PM_train.txt
dataset/PM_test.txt
```

### 3. Treinar o modelo

A prática usual é:

* usar `PM_train.txt` para treinamento;
* separar validação e ajuste de hiperparâmetros;
* definir uma métrica para prever falhas no horizonte de 20 ciclos;
* testar abordagens como regressão, modelos baseados em árvore ou ensembles.

### 4. Gerar as previsões

A saída esperada é um arquivo contendo uma coluna de previsão para cada ativo do conjunto de teste, com uma linha por ativo, em formato similar ao arquivo `exemplo_submissao.csv`.

Exemplo de estrutura esperada:

```csv
predicted
0.93
0.71
0.46
```

Ou, em uma abordagem de RUL:

```csv
rul
28
17
9
```

---

## ✅ Critérios de Sucesso

A solução é considerada bem-sucedida quando ela:

* identifica ativos em risco com antecedência suficiente;
* apresenta desempenho superior ao processo ingênuo de troca por tempo fixo;
* reduz custos operacionais sem gerar indisponibilidade excessiva;
* oferece linguagem clara para apresentação aos stakeholders da operação.

---

## 📈 Métricas Relevantes

Durante a validação, as métricas mais importantes podem incluir:

* acurácia;
* precisão;
* recall;
* F1-score;
* ROC-AUC;
* erro de predição para RUL;
* custo total de manutenção comparado ao cenário atual.

---

## 💡 Recomendações de Uso Prático

A equipe de manutenção pode usar o modelo para:

* priorizar inspeções em ativos com maior risco;
* calendarizar intervenções antes da falha;
* ajustar o plano de manutenção com base em condições reais do equipamento;
* reduzir paradas não programadas e gastos com manutenção preventiva excessiva.

---

## 📝 Observação

Este repositório reúne o material do estudo de caso de manutenção preditiva, incluindo a base de dados, anotações e notebooks de exploração. O foco é demonstrar como transformar dados operacionais em uma solução de manutenção preditiva capaz de embasar decisões de negócio e operação industrial.

<br>

[⬆️ Voltar ao topo](#top) | [🇺🇸 Read in English](#en)

<br>

---

<br>

<a id="en"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

# 🇺🇸 Predictive Maintenance for Industrial Assets - Paper CO

This project aims to support predictive maintenance decisions for industrial assets, focusing on predicting failures before they happen and reducing operating costs. The core goal is to evaluate the feasibility of a failure prediction model and, ideally, estimate the remaining useful life (RUL) of assets with a forecast window of at least 20 cycles.

The scenario is inspired by a cellulose and paper production environment, where preventive maintenance based only on calendar time can lead to excessive inspections, unnecessary spending, and still fail to prevent unexpected equipment downtime.

---

## 🎯 Project Goal

Paper CO needs to reduce maintenance costs without compromising asset availability. To do so, the challenge is to answer three key questions:

* Is it possible to predict failures early enough to act before breakdowns happen?
* Which indicator is more useful for maintenance decisions: failure risk, probability of failure in 20 cycles, or remaining useful life (RUL)?
* How can this model replace or complement a fixed-interval replacement policy?

---

## 📌 Business Context

The pulp and paper industry operates under strong cost pressure and competitive market conditions. Over-maintenance increases costs without adding value, while delayed maintenance can create unplanned outages, lost production, and safety risks.

In this context, predictive maintenance becomes a strategic approach: using operational and sensor data to detect degradation and schedule interventions at the right time.

---

## 🧠 Expected Deliverables

The project aims to produce:

* exploratory analysis of asset data;
* identification of failure patterns and degradation signals;
* predictive modeling for failure or RUL;
* quantitative evaluation of model performance;
* comparison against a naive fixed-interval maintenance policy;
* recommendations for practical use by maintenance and operations teams.

---

## 🗂️ Repository Structure

```text
.
├── dataset/
│   ├── PM_train.txt          # Training data
│   ├── PM_test.txt           # Test data
│   └── ...
├── anotacoes.py              # Project notes and technical context
├── exemplo_submissao.csv     # Example submission format
├── note-suzano.ipynb         # Main notebook for exploratory analysis and modeling
├── note-feat-imp.ipynb       # Additional experiments on feature importance
├── Case Manutenção Preditiva.zip
├── Complete Case Pulp and Paper - Predictive Maintanance.docx
├── Complete Case Pulp and Paper - Predictive Maintanance_pt.docx
└── README.md
```

---

## 📊 Data Dictionary

The training and test datasets contain information by operating cycle for each asset. The general structure includes:

| Field | Description |
| :--- | :--- |
| `id_recurso` | Asset identifier. Each sequence represents a complete operational life until failure. |
| `tmp_exe` | Operating time / cycle execution counter. |
| `cfg1`, `cfg2`, `cfg3` | Operational configuration settings. |
| `tag1` to `tag21` | Sensor readings or physical indicators associated with equipment behavior. |

The dataset is provided as whitespace-separated text with no explicit header and is treated as a time-series table per asset under operating conditions.

---

## 🔍 Project Workflow

1. Read and clean the training data.
2. Perform exploratory analysis of distributions and failure patterns.
3. Extract meaningful signals by asset and by cycle.
4. Build a supervised target (failure within 20 cycles or RUL).
5. Train machine learning models.
6. Validate with relevant classification/regression metrics.
7. Compare the model against a fixed-schedule maintenance policy.
8. Generate the final submission file and presentation outputs.

---

## 🧪 Technologies and Tools

The analysis was developed using a typical Python data science stack:

* Python 3
* NumPy
* pandas
* scikit-learn
* matplotlib
* seaborn
* Jupyter Notebook

---

## ⚙️ Prerequisites

To reproduce the analysis locally, it is recommended to set up a Python environment and install the dependencies:

```bash
python --version
```

Then:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install jupyter pandas numpy scikit-learn matplotlib seaborn
```

---

## ▶️ How to Run

### 1. Launch the analysis environment

```bash
jupyter notebook
```

Or:

```bash
jupyter lab
```

### 2. Load the data

The main input files are in `dataset/`:

```text
dataset/PM_train.txt
dataset/PM_test.txt
```

### 3. Train the model

The usual workflow is:

* use `PM_train.txt` for training;
* split into validation and tuning subsets;
* define a target based on failure within 20 cycles or RUL;
* test approaches such as regression, tree-based models, or ensembles.

### 4. Generate predictions

The expected output is a file with one prediction per asset in the test set, with one row per asset, similar to `exemplo_submissao.csv`.

Example structure:

```csv
predicted
0.93
0.71
0.46
```

Or for a RUL approach:

```csv
rul
28
17
9
```

---

## ✅ Success Criteria

The solution is considered successful when it:

* identifies at-risk assets early enough;
* outperforms a naive fixed-interval replacement process;
* reduces operational costs without excessive downtime;
* provides clear business-oriented insights for stakeholders.

---

## 📈 Relevant Metrics

During validation, the most relevant metrics may include:

* accuracy;
* precision;
* recall;
* F1-score;
* ROC-AUC;
* prediction error for RUL;
* total maintenance cost compared to the current policy.

---

## 💡 Practical Recommendations

The maintenance team can use the model to:

* prioritize inspections for higher-risk assets;
* schedule interventions before failures occur;
* adapt maintenance planning based on actual equipment condition;
* reduce unexpected stoppages and excessive preventive spending.

---

## 📝 Note

This repository contains the case-study material for predictive maintenance, including the dataset, notes, and exploratory notebooks. The focus is to demonstrate how operational data can be turned into a predictive maintenance solution that supports strategic decisions in industrial operations.

<br>

[⬆️ Back to top](#top) | [🇧🇷 Ler em Português](#pt-br)

