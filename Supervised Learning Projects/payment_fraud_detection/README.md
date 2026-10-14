<a id="top"></a>

🌐 **Language / Idioma:** [🇺🇸 English (EN)](#en) | [🇧🇷 Português (PT-BR)](#pt-br)

---

<a id="en"></a>

# 🇺🇸 Payment Fraud Detection

A data analysis and machine learning project focused on identifying fraudulent transactions in the synthetic **PaySim** dataset. The project explores transaction patterns, investigates feature importance, trains classifiers to predict fraud, and interprets the results from both model and business perspectives.

---

## 🚀 Project Highlights

* **Exploratory Data Analysis:** Examines transaction features, transaction types, amounts, and patterns related to fraud.
* **Feature Importance and Explainability:** Uses feature importance and SHAP analysis, including summary plots and correlations between numerical features.
* **Fraud Classification:** Trains models to predict the `isFraud` target and evaluates their performance on a test set.
* **Business-Oriented Analysis:** Interprets the model results and discusses their implications for fraud detection.

---

## 📂 Project Structure

```text
├── paysim.csv                             # Transaction dataset in CSV format
├── paysim.xlsx                            # Transaction dataset in Excel format
├── describe.csv                           # Dataset feature descriptions
├── 1_infra-dataset-analysis.ipynb          # Exploratory data analysis
├── 2_infracom-feature-importance.ipynb     # Feature importance and SHAP analysis
├── 3_infracom-model-creation.ipynb          # Model creation and evaluation
├── 4_infracom-model-analysis.ipynb          # Results analysis and conclusions
└── README.md
```

---

## 📊 Dataset

The project uses the synthetic PaySim dataset, which simulates financial transactions. The dataset reference used in this project is available on [Kaggle](https://www.kaggle.com/code/kartik2112/fraud-detection-on-paysim-dataset).

The prediction target is `isFraud`. The data also includes `isFlaggedFraud`, a flag associated with the dataset's business rule for identifying certain large transfers.

| Feature | Description |
| :--- | :--- |
| `step` | Time step in the simulation; one step represents one hour. |
| `type` | Transaction type, such as `CASH-IN`, `CASH-OUT`, `DEBIT`, `PAYMENT`, or `TRANSFER`. |
| `amount` | Transaction amount in local currency. |
| `nameOrig` | Identifier of the customer initiating the transaction. |
| `oldbalanceOrg` / `newbalanceOrig` | Origin account balance before / after the transaction. |
| `nameDest` | Identifier of the transaction recipient. |
| `oldbalanceDest` / `newbalanceDest` | Recipient account balance before / after the transaction. |
| `isFraud` | Target label indicating a fraudulent transaction. |
| `isFlaggedFraud` | Flag for transactions meeting a specific business rule. |

See [`describe.csv`](./describe.csv) for additional dataset descriptions.

---

## 🛠️ Requirements

* Python with Jupyter Notebook, JupyterLab, or VS Code notebook support.
* Python libraries used in the notebooks include pandas, scikit-learn, XGBoost, and SHAP, along with the standard data analysis and visualization stack.

> **Note:** The notebooks were originally prepared in a Kaggle environment. Update any Kaggle-specific input paths to point to `paysim.csv` and `describe.csv` in this directory when running them locally.

---

## ⚙️ Setup

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2. Install the notebook dependencies

```bash
pip install jupyter pandas scikit-learn xgboost shap
```

Install any additional libraries requested by the notebooks in your environment.

---

## ▶️ How to Explore the Project

Open the notebooks in the following order and run their cells:

1. [`1_infra-dataset-analysis.ipynb`](./1_infra-dataset-analysis.ipynb) — explores the dataset, its features, transaction types, and amounts.
2. [`2_infracom-feature-importance.ipynb`](./2_infracom-feature-importance.ipynb) — investigates feature importance, SHAP explanations, summary plots, and correlations.
3. [`3_infracom-model-creation.ipynb`](./3_infracom-model-creation.ipynb) — prepares the data, creates classifiers for `isFraud`, and evaluates their performance.
4. [`4_infracom-model-analysis.ipynb`](./4_infracom-model-analysis.ipynb) — interprets the model results and presents final conclusions.

Launch Jupyter from the project directory:

```bash
jupyter lab
```

---

## 🔧 Modeling and Evaluation

The modeling notebook uses a train/test split and evaluates fraud classification with metrics including precision, recall, F1-score, and a confusion matrix. These metrics help assess detection quality while accounting for the importance of identifying fraudulent transactions. Feature analysis is explored separately in the feature-importance notebook.

---

[⬆️ Back to top](#top) | [🇧🇷 Ler em Português](#pt-br)

---

<a id="pt-br"></a>

# 🇧🇷 Detecção de Fraudes em Pagamentos

Projeto de análise de dados e aprendizado de máquina voltado à identificação de transações fraudulentas no conjunto sintético **PaySim**. O projeto explora padrões das transações, investiga a importância das variáveis, treina classificadores para prever fraudes e interpreta os resultados sob as perspectivas do modelo e do negócio.

---

## 🚀 Destaques do Projeto

* **Análise Exploratória:** Investiga as variáveis das transações, os tipos de operação, os valores e os padrões relacionados a fraudes.
* **Importância e Explicabilidade das Variáveis:** Utiliza importância de variáveis e análise SHAP, incluindo gráficos de resumo e correlações entre variáveis numéricas.
* **Classificação de Fraudes:** Treina modelos para prever o alvo `isFraud` e avalia seu desempenho em um conjunto de teste.
* **Análise Orientada ao Negócio:** Interpreta os resultados do modelo e discute suas implicações para a detecção de fraudes.

---

## 📂 Estrutura do Projeto

```text
├── paysim.csv                             # Conjunto de transações em formato CSV
├── paysim.xlsx                            # Conjunto de transações em formato Excel
├── describe.csv                           # Descrição das variáveis do conjunto
├── 1_infra-dataset-analysis.ipynb          # Análise exploratória dos dados
├── 2_infracom-feature-importance.ipynb     # Análise de importância e SHAP
├── 3_infracom-model-creation.ipynb          # Criação e avaliação do modelo
├── 4_infracom-model-analysis.ipynb          # Análise dos resultados e conclusões
└── README.md
```

---

## 📊 Conjunto de Dados

O projeto utiliza o conjunto sintético PaySim, que simula transações financeiras. A referência do conjunto de dados usada neste projeto está disponível no [Kaggle](https://www.kaggle.com/code/kartik2112/fraud-detection-on-paysim-dataset).

O alvo da previsão é `isFraud`. Os dados também incluem `isFlaggedFraud`, uma sinalização associada à regra de negócio do conjunto para identificar determinadas transferências de valor elevado.

| Variável | Descrição |
| :--- | :--- |
| `step` | Passo de tempo da simulação; cada passo representa uma hora. |
| `type` | Tipo de transação, como `CASH-IN`, `CASH-OUT`, `DEBIT`, `PAYMENT` ou `TRANSFER`. |
| `amount` | Valor da transação em moeda local. |
| `nameOrig` | Identificador do cliente que iniciou a transação. |
| `oldbalanceOrg` / `newbalanceOrig` | Saldo da conta de origem antes / depois da transação. |
| `nameDest` | Identificador do destinatário da transação. |
| `oldbalanceDest` / `newbalanceDest` | Saldo da conta de destino antes / depois da transação. |
| `isFraud` | Rótulo-alvo que indica uma transação fraudulenta. |
| `isFlaggedFraud` | Sinalização de transações que atendem a uma regra de negócio específica. |

Consulte [`describe.csv`](./describe.csv) para ver descrições adicionais das variáveis.

---

## 🛠️ Requisitos

* Python com Jupyter Notebook, JupyterLab ou suporte a notebooks no VS Code.
* As bibliotecas usadas nos notebooks incluem pandas, scikit-learn, XGBoost e SHAP, além das bibliotecas usuais de análise e visualização de dados.

> **Nota:** Os notebooks foram preparados originalmente em um ambiente Kaggle. Para executá-los localmente, ajuste os caminhos de entrada específicos do Kaggle para apontar para `paysim.csv` e `describe.csv` neste diretório.

---

## ⚙️ Configuração

### 1. Criar e ativar um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2. Instalar as dependências dos notebooks

```bash
pip install jupyter pandas scikit-learn xgboost shap
```

Instale também quaisquer bibliotecas adicionais solicitadas pelos notebooks no seu ambiente.

---

## ▶️ Como Explorar o Projeto

Abra os notebooks na ordem abaixo e execute as células:

1. [`1_infra-dataset-analysis.ipynb`](./1_infra-dataset-analysis.ipynb) — explora o conjunto, suas variáveis, os tipos e os valores das transações.
2. [`2_infracom-feature-importance.ipynb`](./2_infracom-feature-importance.ipynb) — analisa a importância das variáveis, explicações SHAP, gráficos de resumo e correlações.
3. [`3_infracom-model-creation.ipynb`](./3_infracom-model-creation.ipynb) — prepara os dados, cria classificadores para `isFraud` e avalia seu desempenho.
4. [`4_infracom-model-analysis.ipynb`](./4_infracom-model-analysis.ipynb) — interpreta os resultados do modelo e apresenta as conclusões finais.

Inicie o Jupyter a partir do diretório do projeto:

```bash
jupyter lab
```

---

## 🔧 Modelagem e Avaliação

O notebook de modelagem utiliza uma divisão entre treino e teste e avalia a classificação de fraudes com métricas como precisão, recall, F1-score e matriz de confusão. Essas métricas ajudam a analisar a qualidade da detecção, considerando a importância de identificar transações fraudulentas. A análise das variáveis é explorada separadamente no notebook de importância.

---

[⬆️ Voltar ao topo](#top) | [🇺🇸 Read in English](#en)
