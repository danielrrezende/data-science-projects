<a id="top"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

---

<a id="pt-br"></a>

# 🇧🇷 Otimização do Planejamento de Manutenção com Ciência de Dados

## Visão Geral

Este repositório apresenta um estudo de caso de manutenção preditiva aplicado a uma frota de veículos. O problema principal é reduzir os custos de manutenção do sistema de ar dos caminhões por meio de modelos preditivos capazes de identificar veículos com maior risco de falha antes que ocorram intervenções corretivas caras e disruptivas.

A solução foi desenvolvida em um notebook Python com análise exploratória de dados, tratamento de valores ausentes, balanceamento de classes, redução de dimensionalidade e avaliação de modelos de classificação.

---

## 🎯 Contexto do Negócio

Uma empresa de transporte observou aumento significativo nos custos de manutenção do sistema de ar, mesmo mantendo a frota relativamente estável. Esse cenário gera impacto financeiro direto:

- Se um caminhão é enviado para manutenção sem defeito, o custo de inspeção é em média de US$ 10.
- Se o veículo apresenta defeito no sistema de ar e recebe manutenção preventiva, o custo é de aproximadamente US$ 25.
- Se uma falha não é detectada a tempo, a empresa incorre em custos de manutenção corretiva de cerca de US$ 500, além dos prejuízos operacionais causados por paralisações.

O objetivo do projeto é responder: "Como reduzir custos com manutenção do sistema de ar usando dados e inteligência artificial?"

---

## 📌 Objetivos do Projeto

1. Identificar os principais fatores associados a falhas no sistema de ar.
2. Construir um modelo preditivo para classificar veículos em risco.
3. Comparar diferentes abordagens de modelagem e validação.
4. Relacionar métricas técnicas com valor de negócio e impacto financeiro.
5. Apoiar a decisão de manutenção preventiva com base em evidências.

---

## 📦 Estrutura do Repositório

```text
maintenance_planning/
├── README.md                             # Documentação do projeto
├── note-model.ipynb                      # Notebook principal com análise e modelagem
├── dataset/
│   ├── air_system_previous_years.rar     # Dados históricos antes de 2022
│   └── air_system_present_year.rar       # Dados do ano atual para avaliação
├── Challenge description answered.pdf    # Enunciado do desafio em PDF
├── .gitignore                            # Arquivos locais e temporários
└── .venv/                                # Ambiente virtual do usuário (opcional)
```

> O projeto é focado em notebook de análise e experimentação, e não em uma aplicação web ou API separada.

---

## 📊 Base de Dados

Os dados disponíveis consistem em registros históricos de manutenção, com colunas codificadas para preservar confidencialidade. Os arquivos do projeto são:

- `air_system_previous_years.rar` — dados históricos para treinamento e validação.
- `air_system_present_year.rar` — dados do período atual para avaliação final.

Observações importantes:

- Valores ausentes são representados por `na`.
- A variável alvo está na coluna `class`:
  - `pos` = defeito no sistema de ar
  - `neg` = defeito em outro sistema ou ausência de defeito relevante

---

## 🧠 Metodologia Adotada

O notebook segue uma pipeline clássica de ciência de dados, com as seguintes etapas:

1. Importação e exploração inicial dos dados
2. Análise descritiva e perfilamento das variáveis
3. Tratamento de valores ausentes
4. Preparação de variáveis numéricas e categóricas
5. Imputação por KNN (`KNNImputer`)
6. Balanceamento da classe alvo com `SMOTE`
7. Redução de dimensionalidade com `PCA`
8. Treinamento de modelos de classificação
9. Validação cruzada e avaliação com métricas relevantes
10. Interpretação dos resultados e análise de impacto financeiro

---

## 🧪 Modelos e Técnicas Aplicadas

Os principais algoritmos e técnicas usadas incluem:

- `RandomForestClassifier`
- `GradientBoostingClassifier`
- `KNNImputer`
- `SMOTE`
- `PCA`
- `cross_validate`
- `Pipeline` e `ColumnTransformer` do scikit-learn

A pipeline do notebook foi concebida de forma semelhante a este exemplo:

```python
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('imputation', KNNImputer()),
    ('smote', SMOTE(random_state=42, n_jobs=-1)),
    ('PCA', PCA(n_components=30)),
    ('model', RandomForestClassifier(random_state=2048, n_jobs=-1))
])
```

---

## 📈 Métricas Técnicas

Como o problema combina custo operacional e desbalanceamento de classes, as métricas mais relevantes são:

- `Precision` — proporção de verdadeiros positivos entre os diagnósticos positivos.
- `Recall` — capacidade de capturar defeitos reais.
- `F1-score` — equilíbrio entre precisão e recall.
- `ROC-AUC` — capacidade de separação entre as classes.
- `Accuracy` — métrica complementar, mas insuficiente isoladamente em dados desbalanceados.

Em manutenção preditiva, precisão e recall são especialmente relevantes porque:

- falsos positivos geram inspeções desnecessárias;
- falsos negativos podem gerar falhas corretivas muito caras.

---

## 💰 Métrica de Negócio

A métrica central de negócio é a redução de custos operacionais com manutenção do sistema de ar. Em termos práticos, o modelo deve:

- diminuir intervenções desnecessárias;
- antecipar falhas antes que ocorram paradas inesperadas;
- priorizar manutenção preventiva em veículos de maior risco;
- maximizar o retorno financeiro ao evitar gastos corretivos emergenciais.

---

## 🛠️ Como Executar o Projeto

### 1. Extrair os dados

Os arquivos de dados estão compactados em `.rar`. Extraia-os com um utilitário compatível:

```bash
unrar x dataset/air_system_previous_years.rar
unrar x dataset/air_system_present_year.rar
```

Se o `unrar` não estiver disponível, utilize `7z` ou outra ferramenta equivalente.

### 2. Preparar o ambiente Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Caso o repositório não tenha um `requirements.txt`, instale manualmente os pacotes usados no notebook, como `pandas`, `numpy`, `scikit-learn`, `imbalanced-learn`, `matplotlib`, `seaborn` e `ydata-profiling`.

### 3. Abrir o notebook

```bash
jupyter notebook
```

Em seguida, abra o arquivo `note-model.ipynb` e execute as células na ordem.

---

## 🔍 Interpretação dos Resultados

A principal proposta do modelo é permitir decisões mais inteligentes de manutenção, em vez de agir apenas de forma reativa. Em outras palavras:

- o modelo ajuda na priorização de inspeções;
- reduz desperdícios em manutenção preventiva indiscriminada;
- facilita a explicação das variáveis mais associadas ao risco de falha;
- conecta desempenho técnico com valor operacional para a empresa.

---

## ✅ Conclusão

Este projeto mostra uma aplicação realista de ciência de dados no contexto de manutenção industrial. A combinação de análise exploratória, imputação, balanceamento, redução de dimensionalidade e modelagem preditiva oferece uma base sólida para apoiar decisões estratégicas de manutenção, com foco direto em redução de custos e melhoria da operação da frota.

---

[⬆️ Voltar ao topo](#top) | [🇺🇸 Read in English](#en)

---

<a id="en"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

# 🇺🇸 Maintenance Planning Optimization with Data Science

## Overview

This repository presents a predictive maintenance use case for a fleet of vehicles. The main goal is to reduce the costs of air-system maintenance by using predictive models that can identify trucks with a higher risk of failure before expensive corrective interventions occur.

The solution was developed in a Python notebook with exploratory data analysis, missing-value treatment, class balancing, dimensionality reduction, and classification model evaluation.

---

## 🎯 Business Context

A transportation company observed a significant increase in air-system maintenance costs while the fleet size remained relatively stable. This creates a direct financial impact:

- If a truck is sent to maintenance without a defect, the inspection cost is about US$ 10.
- If the vehicle has an air-system defect and receives preventive maintenance, the cost is approximately US$ 25.
- If the defect is not detected in time, the company incurs corrective maintenance costs of around US$ 500, in addition to the operational losses caused by downtime.

The project's objective is to answer: "How can we reduce costs related to the air system using data and artificial intelligence?"

---

## 📌 Project Goals

1. Identify the main factors associated with air-system failures.
2. Build a predictive model to classify at-risk vehicles.
3. Compare different modeling and validation approaches.
4. Relate technical metrics to business value and financial impact.
5. Support preventive maintenance decisions with evidence-based insights.

---

## 📦 Repository Structure

```text
maintenance_planning/
├── README.md                             # Project documentation
├── note-model.ipynb                      # Main notebook with analysis and modeling
├── dataset/
│   ├── air_system_previous_years.rar     # Historical data before 2022
│   └── air_system_present_year.rar       # Current-year evaluation data
├── Challenge description answered.pdf    # Project statement in PDF
├── .gitignore                            # Local and temporary files
└── .venv/                                # User virtual environment (optional)
```

> This project focuses on analytical notebooks and experimentation rather than a separate web app or API.

---

## 📊 Dataset

The available data consists of maintenance records with encoded columns to preserve confidentiality. The project files are:

- `air_system_previous_years.rar` — historical data for training and validation.
- `air_system_present_year.rar` — current-period data for final evaluation.

Important notes:

- Missing values are stored as `na`.
- The target variable is in the `class` column:
  - `pos` = air-system defect
  - `neg` = defect in another system or no relevant defect

---

## 🧠 Methodology

The notebook follows a standard data science workflow with these stages:

1. Data import and initial exploration
2. Descriptive analysis and variable profiling
3. Missing-value treatment
4. Preparation of numerical and categorical variables
5. KNN imputation using `KNNImputer`
6. Class balancing with `SMOTE`
7. Dimensionality reduction with `PCA`
8. Classification model training
9. Cross-validation and evaluation using relevant metrics
10. Result interpretation and financial impact analysis

---

## 🧪 Models and Techniques Used

The primary algorithms and techniques include:

- `RandomForestClassifier`
- `GradientBoostingClassifier`
- `KNNImputer`
- `SMOTE`
- `PCA`
- `cross_validate`
- `Pipeline` and `ColumnTransformer` from scikit-learn

The notebook pipeline was designed in a way similar to:

```python
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('imputation', KNNImputer()),
    ('smote', SMOTE(random_state=42, n_jobs=-1)),
    ('PCA', PCA(n_components=30)),
    ('model', RandomForestClassifier(random_state=2048, n_jobs=-1))
])
```

---

## 📈 Technical Metrics

Because the problem combines operational cost with class imbalance, the most relevant metrics are:

- `Precision` — proportion of true positives among predicted positives.
- `Recall` — ability to detect actual failures.
- `F1-score` — balance between precision and recall.
- `ROC-AUC` — ability to separate classes.
- `Accuracy` — useful as a complementary metric, but insufficient alone in imbalanced datasets.

In predictive maintenance, precision and recall are particularly important because:

- false positives generate unnecessary inspections;
- false negatives may lead to very expensive corrective failures.

---

## 💰 Business Metric

The core business metric is the reduction in operational costs related to air-system maintenance. In practice, the model should:

- reduce unnecessary interventions;
- anticipate failures before unexpected downtime occurs;
- prioritize preventive maintenance for higher-risk vehicles;
- maximize financial return by avoiding emergency repair costs.

---

## 🛠️ How to Run the Project

### 1. Extract the data

The dataset files are compressed in `.rar`. Extract them with a compatible utility:

```bash
unrar x dataset/air_system_previous_years.rar
unrar x dataset/air_system_present_year.rar
```

If `unrar` is unavailable, use `7z` or another equivalent archive tool.

### 2. Set up the Python environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> If the repository does not include a `requirements.txt`, install the packages used in the notebook manually, such as `pandas`, `numpy`, `scikit-learn`, `imbalanced-learn`, `matplotlib`, `seaborn`, and `ydata-profiling`.

### 3. Open the notebook

```bash
jupyter notebook
```

Then open `note-model.ipynb` and run the cells in order.

---

## 🔍 Result Interpretation

The main purpose of the model is to support smarter maintenance decisions instead of reacting only after failure. In other words:

- the model helps prioritize inspections;
- reduces waste in indiscriminate preventive maintenance;
- clarifies which variables are most associated with failure risk;
- connects technical performance to operational business value.

---

## ✅ Conclusion

This project demonstrates a realistic application of data science to industrial maintenance. The combination of exploratory analysis, imputation, balancing, dimensionality reduction, and predictive modeling provides a solid foundation for strategic decision-making focused on reducing costs and improving fleet operations.

---

[⬆️ Back to top](#top) | [🇧🇷 Ler em Português](#pt-br)
