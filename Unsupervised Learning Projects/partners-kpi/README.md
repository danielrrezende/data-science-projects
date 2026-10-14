# 📊 Parceiros 360 / Partners 360 (Vivo Telefônica)

🌐 **Idioma / Language:** [🇧🇷 Português](#-português-pt-br) | [🇺🇸 English](#-english-en)

---

# 🇧🇷 Português (PT-BR)

Modelagem de aprendizado não supervisionado e interpretabilidade de modelos para criação e análise de KPIs de risco das lojas parceiras e fornecedores da Vivo Telefônica.

## 🎯 Visão Geral do Projeto

O projeto **Parceiros 360** é um pipeline analítico e preditivo desenvolvido para avaliar a saúde financeira, trabalhista e operacional de parceiros comerciais e fornecedores. 

Utilizando algoritmos de clusterização (**K-Means**) combinados com árvores de decisão (**Random Forest**) e técnicas de explicabilidade (**TreeInterpreter**), o sistema classifica os parceiros em três faixas de risco/desempenho (`BOM` / `RISCO BAIXO`, `MÉDIO` / `RISCO MÉDIO`, `RUIM` / `RISCO ALTO`) e calcula o **percentual de contribuição (de 0 a 100)** de cada variável para a decisão do modelo.

## 🏗️ Arquitetura e Fluxo de Dados

O projeto é estruturado em três etapas principais executadas através de Jupyter Notebooks:

### 1. Extração, Transformação e Carga (ETL)
* **`ETL - Pagamento.ipynb`**: 
  * Processa a base de pagamentos (`02_PAGTO.csv`), agrupando valores por fornecedor, cruza com o cadastro (`nome_fornecedores.xlsx`) e com a base histórica de scores (`01DF_FULL.csv`).
  * Exporta a base consolidada para `intermediate/etl_previsao_pagamentos.xlsx`.
* **`ETL - Comissao.ipynb`**: 
  * Cruza os registros de comissões (`02_COMISSAO.csv`), indicadores quantitativos de risco (`20221017 - TBL_QUANT_COMISSAO.csv`) e dados cadastrais (`nome_fornecedores.xlsx`).
  * Trata valores ausentes (`SEM INDICADOR RISCO`, `SEM FATOR RISCO`) e aplica codificação ordinal (`OrdinalEncoder`) nas variáveis categóricas de risco.
  * Exporta o resultado para `intermediate/etl_previsao_comissao.xlsx`.

### 2. Modelagem e Explicabilidade (Clustering + Feature Contribution)
Em cada frente de análise, os dados passam por normalização `MinMaxScaler(0, 1)` e são submetidos à função `makedf()`, que executa:
1. **Clusterização (`KMeans`)**: Agrupa os dados em 3 clusters (`n_clusters=3`, `init='k-means++'`).
2. **Modelo Substituto (`RandomForestClassifier`)**: Treina uma Random Forest supervisionada tendo os clusters gerados pelo K-Means como *target*.
3. **Explicabilidade (`treeinterpreter`)**: Extrai o peso/contribuição individual de cada *feature* para o cluster atribuído a cada fornecedor, normalizando o impacto em uma escala de `0` a `100` (`_CONTRIBUTION`).

* **`Aliados-KMeans.ipynb`**: Analisa a base `datasets/ALIADOS_KPI.csv` gerando 3 modelos independentes:
  * **KPI A1 (Variação)**: Avalia `MM6`, `HCS_SAP_GT`, `HCS` e `MONITORADO_SIM` → Gera `outputs/previsao_aliados_variacao_kpi1.xlsx`.
  * **KPI A2 (Trabalhista)**: Avalia `QDE_PROC_TRAB`, `HCS_SAP_GT`, `HCS` e `MONITORADO_SIM` → Gera `outputs/previsao_aliados_trabalhista_kpi2.xlsx`.
  * **KPI A3 (Endividamento)**: Avalia passivos de FGTS e INSS (`ATIVA_FGTS`, `PARCELADA_FGTS`, `FGTS_TOTAL`, `ATIVA_INSS`, `PARCELADA_INSS`, `INSS_TOTAL`, `TOTAL_GERAL`) → Gera `outputs/previsao_aliados_endividamento_kpi3.xlsx`.
* **`Pagamento-kmeans.ipynb`**: Avalia utilização de *factoring* e bloqueios financeiros (`MONT_EM_MI`, `TP_PAGTO_BANCO`, `TP_PAGTO_FACTORING`, `TP_PAGTO_FACTORING_MONT_EM_MI`, `BLOQUEIO_NAO`, `BLOQUEIO_NAO_MONT_EM_MI`, `BLOQUEIO_SIM`, `BLOQUEIO_SIM_MONT_EM_MI`) → Gera `outputs/previsao_pagamentos.xlsx`.
* **`comissao-kmeans.ipynb`**: Avalia os indicadores codificados de comissão (`INDICADOR_RISCO_FIN_OE`, `FATOR_RISCO_OE`) → Gera `outputs/previsao_comissao.xlsx`.

### 3. Consolidação Geral (Visão 360)
* **`merge-all-kpi.ipynb`**: Realiza o *outer join* de todas as previsões geradas (`Pagamento`, `Faturamento`, `Comissão`, `Aliados KPI 1`, `Aliados KPI 2` e `Aliados KPI 3`) pelas chaves `RAIZ_CNPJ`, `COMPETENCIA` e `NOME_FORNECEDOR`, unificando todos os indicadores de risco em uma visão 360º única por parceiro.

## 📂 Estrutura de Diretórios Esperada

```text
├── datasets/
│   ├── 01DF_FULL.csv
│   ├── 02_COMISSAO.csv
│   ├── 02_PAGTO.csv
│   ├── 20221017 - TBL_QUANT_COMISSAO.csv
│   ├── ALIADOS_KPI.csv
│   └── nome_fornecedores.xlsx
├── intermediate/
│   ├── etl_previsao_comissao.xlsx
│   └── etl_previsao_pagamentos.xlsx
├── outputs/
│   ├── previsao_aliados_endividamento_kpi3.xlsx
│   ├── previsao_aliados_trabalhista_kpi2.xlsx
│   ├── previsao_aliados_variacao_kpi1.xlsx
│   ├── previsao_comissao.xlsx
│   └── previsao_pagamentos.xlsx
├── ETL - Comissao.ipynb
├── ETL - Pagamento.ipynb
├── Aliados-KMeans.ipynb
├── Pagamento-kmeans.ipynb
├── comissao-kmeans.ipynb
├── merge-all-kpi.ipynb
└── README.md
```

## 🛠️ Pré-requisitos e Instalação

O projeto foi desenvolvido em **Python 3.8+**. Para configurar o ambiente:

```bash
# 1. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou: venv\Scripts\activate (Windows)

# 2. Instale as dependências necessárias
pip install pandas numpy scikit-learn matplotlib seaborn shap treeinterpreter openpyxl python-dateutil
```

## 🚀 Ordem de Execução

Para reproduzir todo o pipeline de dados do início ao fim, execute os notebooks na seguinte sequência:

1. `ETL - Pagamento.ipynb`
2. `ETL - Comissao.ipynb`
3. `Aliados-KMeans.ipynb`
4. `Pagamento-kmeans.ipynb`
5. `comissao-kmeans.ipynb`
6. `merge-all-kpi.ipynb`

---
---

# 🇺🇸 English (EN)

Unsupervised machine learning and model interpretability pipeline designed to create and analyze risk KPIs for Vivo Telefônica's partner stores and suppliers.

## 🎯 Project Overview

The **Parceiros 360 (Partners 360)** project is an analytical and predictive pipeline developed to assess the financial, labor, and operational health of commercial partners and suppliers.

By combining clustering algorithms (**K-Means**) with surrogate decision trees (**Random Forest**) and explainability techniques (**TreeInterpreter**), the system classifies partners into three risk/performance tiers (`BOM` / `LOW RISK`, `MÉDIO` / `MEDIUM RISK`, `RUIM` / `HIGH RISK`) and calculates the **percentage contribution (scaled 0 to 100)** of each feature toward the model's final classification.

## 🏗️ Architecture & Data Pipeline

The project is structured into three main stages executed via Jupyter Notebooks:

### 1. Extract, Transform, and Load (ETL)
* **`ETL - Pagamento.ipynb`**: 
  * Processes raw payment records (`02_PAGTO.csv`), aggregates amounts by supplier, and joins the data with supplier master records (`nome_fornecedores.xlsx`) and historical KPI scores (`01DF_FULL.csv`).
  * Exports the processed dataset to `intermediate/etl_previsao_pagamentos.xlsx`.
* **`ETL - Comissao.ipynb`**: 
  * Merges commission records (`02_COMISSAO.csv`), quantitative risk indicators (`20221017 - TBL_QUANT_COMISSAO.csv`), and supplier registration data (`nome_fornecedores.xlsx`).
  * Handles missing values (`SEM INDICADOR RISCO`, `SEM FATOR RISCO`) and applies ordinal encoding (`OrdinalEncoder`) to categorical risk variables.
  * Exports the processed dataset to `intermediate/etl_previsao_comissao.xlsx`.

### 2. Modeling & Explainability (Clustering + Feature Contribution)
In each analytical track, features are normalized using `MinMaxScaler(0, 1)` and processed through the `makedf()` function, which performs:
1. **Clustering (`KMeans`)**: Segments partners into 3 clusters (`n_clusters=3`, `init='k-means++'`).
2. **Surrogate Modeling (`RandomForestClassifier`)**: Fits a supervised Random Forest classifier using the K-Means cluster assignments as the target variable.
3. **Explainability (`treeinterpreter`)**: Extracts the individual feature contributions for the assigned cluster of each record, scaling the impact from `0` to `100` (`_CONTRIBUTION`).

* **`Aliados-KMeans.ipynb`**: Analyzes `datasets/ALIADOS_KPI.csv` across 3 independent KPI models:
  * **KPI A1 (Variation)**: Evaluates `MM6`, `HCS_SAP_GT`, `HCS`, and `MONITORADO_SIM` → Outputs `outputs/previsao_aliados_variacao_kpi1.xlsx`.
  * **KPI A2 (Labor/Legal)**: Evaluates labor lawsuits and headcount (`QDE_PROC_TRAB`, `HCS_SAP_GT`, `HCS`, `MONITORADO_SIM`) → Outputs `outputs/previsao_aliados_trabalhista_kpi2.xlsx`.
  * **KPI A3 (Indebtedness)**: Evaluates FGTS and INSS tax/social security liabilities (`ATIVA_FGTS`, `PARCELADA_FGTS`, `FGTS_TOTAL`, `ATIVA_INSS`, `PARCELADA_INSS`, `INSS_TOTAL`, `TOTAL_GERAL`) → Outputs `outputs/previsao_aliados_endividamento_kpi3.xlsx`.
* **`Pagamento-kmeans.ipynb`**: Evaluates factoring usage and payment blocks (`MONT_EM_MI`, `TP_PAGTO_BANCO`, `TP_PAGTO_FACTORING`, `TP_PAGTO_FACTORING_MONT_EM_MI`, `BLOQUEIO_NAO`, `BLOQUEIO_NAO_MONT_EM_MI`, `BLOQUEIO_SIM`, `BLOQUEIO_SIM_MONT_EM_MI`) → Outputs `outputs/previsao_pagamentos.xlsx`.
* **`comissao-kmeans.ipynb`**: Evaluates encoded commission risk indicators (`INDICADOR_RISCO_FIN_OE`, `FATOR_RISCO_OE`) → Outputs `outputs/previsao_comissao.xlsx`.

### 3. Master Consolidation (360º View)
* **`merge-all-kpi.ipynb`**: Performs an outer join across all generated predictions (`Payments`, `Billing/Faturamento`, `Commissions`, `Allies KPI 1`, `Allies KPI 2`, and `Allies KPI 3`) on `RAIZ_CNPJ`, `COMPETENCIA`, and `NOME_FORNECEDOR`, unifying all risk indicators into a single 360-degree view per partner.

## 📂 Expected Directory Structure

```text
├── datasets/
│   ├── 01DF_FULL.csv
│   ├── 02_COMISSAO.csv
│   ├── 02_PAGTO.csv
│   ├── 20221017 - TBL_QUANT_COMISSAO.csv
│   ├── ALIADOS_KPI.csv
│   └── nome_fornecedores.xlsx
├── intermediate/
│   ├── etl_previsao_comissao.xlsx
│   └── etl_previsao_pagamentos.xlsx
├── outputs/
│   ├── previsao_aliados_endividamento_kpi3.xlsx
│   ├── previsao_aliados_trabalhista_kpi2.xlsx
│   ├── previsao_aliados_variacao_kpi1.xlsx
│   ├── previsao_comissao.xlsx
│   └── previsao_pagamentos.xlsx
├── ETL - Comissao.ipynb
├── ETL - Pagamento.ipynb
├── Aliados-KMeans.ipynb
├── Pagamento-kmeans.ipynb
├── comissao-kmeans.ipynb
├── merge-all-kpi.ipynb
└── README.md
```

## 🛠️ Prerequisites & Installation

This project was developed using **Python 3.8+**. To set up the environment:

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or: venv\Scripts\activate (Windows)

# 2. Install required dependencies
pip install pandas numpy scikit-learn matplotlib seaborn shap treeinterpreter openpyxl python-dateutil
```

## 🚀 Execution Order

To reproduce the entire data pipeline from start to finish, run the notebooks in the following order:

1. `ETL - Pagamento.ipynb`
2. `ETL - Comissao.ipynb`
3. `Aliados-KMeans.ipynb`
4. `Pagamento-kmeans.ipynb`
5. `comissao-kmeans.ipynb`
6. `merge-all-kpi.ipynb`