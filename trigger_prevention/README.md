<a id="top"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

---

<a id="pt-br"></a>

# 🇧🇷 Segware - Previsão de disparos verdadeiros

Projeto de ciência de dados e machine learning para prever se um disparo de alarme é verdadeiro ou falso, com foco em reduzir deslocamentos desnecessários em empresas de monitoramento.

O contexto do problema é o de uma empresa de monitoramento que recebe eventos de alarmes, câmeras e sensores. Nem todo disparo representa um incidente real: fatores como galhos, animais, tempestades ou testes do cliente podem gerar falsos positivos. O objetivo é classificar corretamente os eventos e apoiar decisões operacionais com maior precisão.

---

## 🎯 Objetivo do projeto

Desenvolver um algoritmo de aprendizado de máquina capaz de prever se um disparo é:

- `0` → falso alarmante / sem sinistro real
- `1` → disparo verdadeiro / sinistro confirmado

A solução considera dados históricos de treinamento, realiza preparação e transformação dos atributos, e avalia a qualidade do modelo por métricas de classificação.

---

## 📌 Descrição do problema

Uma empresa de monitoramento precisa enviar viaturas até a residência ou comércio quando há um disparo de alarme. No entanto, muitos destes eventos são falsos, gerando custos operacionais e logística desnecessária.

Com base nos arquivos `train.csv` e `test.csv`, o projeto busca construir um modelo preditivo que identifique o comportamento mais provável de cada evento, reduzindo erros de classificação e melhorando o atendimento.

---

## 🧠 Abordagem aplicada

A solução usa uma pipeline de pré-processamento e modelagem com foco em dados mistos (numéricos e categóricos):

- análise de dados faltantes (`NaN`)
- definição da variável alvo (`Confirmado`)
- seleção de features relevantes
- separação dos dados em treino e teste
- processamento de variáveis categóricas com `OneHotEncoder`
- padronização de variáveis numéricas com `StandardScaler`
- equilíbrio do dataset com `SMOTE`
- classificação com `LogisticRegression`
- avaliação com matriz de confusão, ROC e relatório de métricas

Este fluxo foi construído a partir do notebook principal `Segware.ipynb`, que documenta a lógica de cada etapa com comentários e explicações.

---

## 📊 Dicionário de dados

| Campo | Descrição |
| :--- | :--- |
| Código do cliente | Identificador único do cliente dentro do sistema |
| Nível de risco | Grau de periculosidade do local, sendo 5 o mais alto |
| Possui servidor CFTV | Indica se o cliente possui monitoramento por câmeras/imagens (`0` = não, `1` = sim) |
| Pessoa Física, Jurídica ou Órgão Público | `0` = jurídica, `1` = física, `2` = órgão público |
| Estado | UF do cliente |
| Cidade | Cidade do cliente |
| Bairro | Bairro do cliente |
| Data/hora | Data e hora da ocorrência do evento |
| Código do evento | Código do evento enviado pelo sistema |
| Confirmado | Indicador do sinistro real (`0` = não, `1` = sim) |

---

## 🗂️ Estrutura do projeto

```text
trigger_prevention/
├── README.md                  # Documentação do projeto
├── Segware.ipynb              # Notebook principal com a análise e modelagem
├── train.csv                  # Base de dados de treinamento
├── test.csv                   # Base de dados de teste
├── submission_test.csv         # Arquivo de predição gerado para submissão
└── .gitignore                 # Arquivos e diretórios ignorados pelo Git
```

---

## ⚙️ Requisitos

- Python 3.9+
- Jupyter Notebook / JupyterLab
- Bibliotecas: `pandas`, `numpy`, `scikit-learn`, `imblearn`, `matplotlib`, `seaborn`, `scikit-plot`

### Instalação

```bash
pip install pandas numpy scikit-learn imbalanced-learn matplotlib seaborn scikit-plot
```

---

## ▶️ Como executar

### 1. Abrir o notebook

```bash
jupyter notebook Segware.ipynb
```

### 2. Rodar as células em sequência

O notebook realiza:

1. leitura dos arquivos CSV
2. checagem de dados faltantes
3. definição do alvo e das features
4. separação entre treino e teste
5. pré-processamento dos dados
6. treinamento do modelo
7. geração de previsões
8. avaliação de métricas
9. exportação do arquivo de saída

---

## 🧪 Pipeline de modelagem

A abordagem do projeto foi organizada em etapas bem definidas:

### 1) Leitura e validação dos dados

Os dados são carregados em `pandas` e a presença de valores nulos é verificada com `isna()`. Essa etapa é essencial para garantir a integridade da base antes do treinamento.

### 2) Definição do target e das features

- `y = train.Confirmado` → variável alvo
- `X = train[features]` → atributos utilizados para previsão

As features selecionadas incluem risco, presença de CFTV, tipo da pessoa, cidade, bairro, data/hora e código do evento.

### 3) Separação dos dados

A base foi dividida em treino e teste com `train_test_split`, usando 60% para treino e 40% para avaliação.

### 4) Pré-processamento

- variáveis numéricas: padronização via `StandardScaler`
- variáveis categóricas: transformação para binárias via `OneHotEncoder`
- `ColumnTransformer` combina os passos de forma automatizada

### 5) Tratamento de classes desbalanceadas

A base possui um número menor de eventos reais, o que pode causar enviesamento do modelo. Para isso, foi usado `SMOTE` dentro do pipeline, aumentando a representação da classe positiva no treinamento.

### 6) Modelo

O modelo escolhido foi `LogisticRegression`, por ser simples, interpretável e adequado para classificação binária.

### 7) Predição e avaliação

A etapa final calcula:

- `preds` → previsões do modelo
- `confusion_matrix` → matriz de confusão
- `classification_report` → precision, recall, f1-score e support
- `plot_roc` → curva ROC para medir a capacidade de distinção entre classes

---

## 📈 Métricas e desempenho

De acordo com a análise documentada no notebook, o modelo apresenta bom desempenho, com destaque para a curva ROC e para a capacidade de distinguir corretamente disparos verdadeiros e falsos.

O notebook informa que a área sob a curva (AUC) da ROC está próxima de 96%, indicando alta capacidade discriminativa do classificador.

---

## 📤 Saída esperada

O projeto gera um arquivo de predição para submissão, com a coluna de resposta indicando se o disparo foi classificado como verdadeiro ou falso.

---

## ✅ Conclusão

Este projeto demonstra uma aplicação prática de machine learning para um problema operacional real em monitoramento de segurança. A combinação de limpeza de dados, engenharia de features, tratamento de desbalanceamento e validação por métricas de classificação resulta em uma solução útil para reduzir custos e melhorar a tomada de decisão.

---

[⬆️ Voltar ao topo](#top) | [🇺🇸 Read in English](#en)

---

<a id="en"></a>

# 🇺🇸 Segware - True trigger prediction

A data science and machine learning project designed to predict whether an alarm trigger is genuine or false, with the goal of reducing unnecessary field dispatches in monitoring companies.

The business context is a security monitoring company handling events from alarms, cameras, and sensors. Not every trigger corresponds to a real incident: branches moving in the wind, animals, storms, or customer tests can all generate false alarms. The goal is to correctly classify events and support operational decisions with better accuracy.

---

## 🎯 Project objective

Develop a machine learning algorithm capable of predicting whether a trigger is:

- `0` → false alarm / no real incident
- `1` → true trigger / confirmed incident

The solution uses historical training data, prepares and transforms the attributes, and evaluates model quality with classification metrics.

---

## 📌 Problem description

A monitoring company must send patrol vehicles to homes or businesses whenever an alarm is triggered. However, many of these events are false, which creates unnecessary operational and logistical costs.

Based on the `train.csv` and `test.csv` files, the project aims to build a predictive model that identifies the most likely behavior of each event, reducing misclassification and improving service quality.

---

## 🧠 Applied approach

The solution uses a preprocessing and modeling pipeline focused on mixed-type data (numeric and categorical):

- missing-data analysis (`NaN`)
- target definition (`Confirmado`)
- relevant feature selection
- split into training and testing sets
- categorical encoding with `OneHotEncoder`
- numerical scaling with `StandardScaler`
- imbalance handling with `SMOTE`
- classification with `LogisticRegression`
- evaluation using confusion matrix, ROC, and classification reports

This workflow was implemented in the main notebook `Segware.ipynb`, which documents the logic and decisions behind each stage.

---

## 📊 Data dictionary

| Field | Description |
| :--- | :--- |
| Client code | Unique identifier of the customer in the system |
| Risk level | Severity of the location, where 5 is the highest |
| Has CFTV server | Indicates whether the customer has image monitoring (`0` = no, `1` = yes) |
| Person type | `0` = legal entity, `1` = individual, `2` = public body |
| State | Customer state |
| City | Customer city |
| Neighborhood | Customer neighborhood |
| Date/time | Date and time of the event |
| Event code | Event code sent by the system |
| Confirmed | Indicates whether a real incident occurred (`0` = no, `1` = yes) |

---

## 🗂️ Project structure

```text
trigger_prevention/
├── README.md                  # Project documentation
├── Segware.ipynb              # Main notebook with analysis and modeling
├── train.csv                  # Training dataset
├── test.csv                   # Test dataset
├── submission_test.csv         # Prediction file generated for submission
└── .gitignore                 # Git-ignored files and directories
```

---

## ⚙️ Requirements

- Python 3.9+
- Jupyter Notebook / JupyterLab
- Libraries: `pandas`, `numpy`, `scikit-learn`, `imblearn`, `matplotlib`, `seaborn`, `scikit-plot`

### Installation

```bash
pip install pandas numpy scikit-learn imbalanced-learn matplotlib seaborn scikit-plot
```

---

## ▶️ How to run

### 1. Open the notebook

```bash
jupyter notebook Segware.ipynb
```

### 2. Run the cells in order

The notebook performs:

1. CSV reading
2. missing value checks
3. target and feature definition
4. train/test split
5. preprocessing
6. model training
7. prediction generation
8. performance evaluation
9. output export

---

## 🧪 Modeling pipeline

The project workflow is organized into clear steps:

### 1) Data loading and validation

Data is loaded with `pandas`, and missing values are checked with `isna()`. This step ensures the integrity of the dataset before training.

### 2) Target and feature definition

- `y = train.Confirmado` → target variable
- `X = train[features]` → attributes used for prediction

The chosen features include risk, CFTV presence, customer type, city, neighborhood, date/time, and event code.

### 3) Data split

The dataset is divided into training and testing sets using `train_test_split`, with 60% for training and 40% for evaluation.

### 4) Preprocessing

- numeric variables: standardization with `StandardScaler`
- categorical variables: one-hot encoding with `OneHotEncoder`
- `ColumnTransformer` combines both transformations automatically

### 5) Class imbalance handling

The dataset contains fewer real incidents than non-incidents, which can bias the model. To address this, `SMOTE` is applied within the pipeline to improve representation of the positive class.

### 6) Model

The selected model is `LogisticRegression`, chosen for being simple, interpretable, and suitable for binary classification tasks.

### 7) Prediction and evaluation

The final stage computes:

- `preds` → model predictions
- `confusion_matrix` → confusion matrix
- `classification_report` → precision, recall, F1-score, and support
- `plot_roc` → ROC curve to measure class separability

---

## 📈 Performance and metrics

According to the analysis documented in the notebook, the model shows strong performance, particularly in distinguishing true triggers from false alarms. The notebook reports an ROC curve area close to 96%, indicating high discriminative power.

---

## 📤 Expected output

The project generates a prediction file for submission, including the response column indicating whether the trigger was classified as true or false.

---

## ✅ Conclusion

This project demonstrates a practical application of machine learning to a real operational problem in security monitoring. By combining data cleaning, feature selection, imbalance handling, and rigorous validation, the solution helps reduce unnecessary dispatches and improve decision-making.

---

[⬆️ Back to top](#top) | [🇧🇷 Voltar para PT-BR](#pt-br)

