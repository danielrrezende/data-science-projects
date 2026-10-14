<a id="top"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

---

<a id="pt-br"></a>

# 🇧🇷 Previsão de Troca de Smartphones

Projeto de *machine learning* supervisionado para identificar clientes com propensão a trocar de aparelho e prever o tempo de uso (*aging*) associado à troca. O fluxo é implementado em notebooks Jupyter e inclui análises exploratórias, treinamento e avaliação de modelos, além de experimentos específicos para aparelhos Apple.

## 🚀 Objetivos e fluxo de modelagem

O processo é dividido em duas etapas:

1. **Classificação da troca:** prevê o alvo `trocou_aparelho`.
2. **Previsão do tempo de uso:** para os clientes classificados como propensos à troca, prevê `aging_aparelho`, a faixa/valor de tempo de uso usada nos dados.

Os notebooks de treinamento usam pipelines do scikit-learn e XGBoost. O pipeline também aplica SMOTE para tratar o desbalanceamento de classes. Os modelos gerais e os específicos para Apple são treinados separadamente.

## 📂 Estrutura do projeto

```text
├── ta-analysis.ipynb                 # Análise exploratória da base geral
├── ta-analysis-apple.ipynb           # Análise exploratória da base Apple
├── ta-feat-imp-corr.ipynb            # Importância de variáveis e correlações
├── ta-feat-imp-corr-apple.ipynb      # Importância e correlações para Apple
├── ta-training-model.ipynb           # Treinamento dos modelos gerais
├── ta-training-model-apple.ipynb     # Treinamento dos modelos Apple
├── ta-load-model.ipynb               # Carregamento e avaliação dos modelos gerais
├── ta-load-model-apple.ipynb         # Carregamento e avaliação dos modelos Apple
├── compare-avg-pred.ipynb            # Comparação de previsões na base geral
├── compare-avg-pred-apple.ipynb      # Comparação de previsões para Apple
├── merge-all-kpi.ipynb               # Consolidação de indicadores
├── models/
│   ├── model_trocou_aparelho.pk      # Classificador geral de propensão à troca
│   ├── model_aging.pk                # Classificador geral de aging
│   ├── model_trocou_aparelho_apple.pk # Classificador Apple de propensão à troca
│   └── model_aging_apple.pk          # Classificador Apple de aging
└── outros_notebooks/                 # Análises e experimentos anteriores
```

## 📊 Dados

Os arquivos de dados usados nos notebooks **não estão incluídos neste repositório**. Os notebooks apontam para bases CSV externas (originalmente configuradas em caminhos do Kaggle), então ajuste as variáveis de caminho no notebook para indicar a localização dos seus arquivos.

As bases precisam conter os campos utilizados no respectivo fluxo, incluindo os alvos `trocou_aparelho` e `aging_aparelho` e as variáveis de cliente/aparelho selecionadas no notebook. Os experimentos Apple aplicam filtros próprios; verifique as células de preparação de dados antes de reutilizar uma base diferente.

> Os dados podem conter informações de clientes. Use apenas bases para as quais você tenha autorização de acesso e tratamento, seguindo os controles de privacidade aplicáveis.

## 🛠️ Tecnologias

* Python e Jupyter Notebook
* `pandas` e `numpy` para manipulação dos dados
* `matplotlib` e `seaborn` para visualização
* `scikit-learn`, `imbalanced-learn` e `xgboost` para preparação e modelagem
* `dill` para serialização dos pipelines treinados

## ⚙️ Instalação e configuração

Crie um ambiente virtual, ative-o e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate

pip install jupyter pandas numpy matplotlib seaborn scikit-learn imbalanced-learn xgboost dill scikit-plot python-dateutil
```

Inicie o Jupyter:

```bash
jupyter lab
```

Abra o notebook desejado e atualize os caminhos para os arquivos CSV. Os notebooks de treinamento salvam os modelos na pasta `models/`; confirme o diretório de saída nas células de serialização se executar o notebook a partir de outro local.

## ▶️ Como executar

Para reproduzir o fluxo principal:

1. Execute `ta-analysis.ipynb` para inspecionar e preparar os dados gerais.
2. Execute `ta-training-model.ipynb` para treinar e salvar os classificadores gerais de troca e aging.
3. Use `ta-load-model.ipynb` para carregar e avaliar os modelos salvos em uma base de validação.
4. Consulte `compare-avg-pred.ipynb` para comparar previsões e `merge-all-kpi.ipynb` para consolidar indicadores, quando aplicável.

Para a análise específica de Apple, siga os notebooks correspondentes com o sufixo `-apple`.

Os arquivos `.pk` são artefatos serializados dos pipelines; para usá-los, mantenha as dependências e versões compatíveis com as utilizadas durante o treinamento. Não carregue artefatos serializados provenientes de fontes não confiáveis.

## 📈 Avaliação

Os notebooks incluem métricas e visualizações como *classification report*, matriz de confusão e ROC/AUC para avaliar os modelos. Os resultados dependem da base, dos filtros e da divisão de treino/validação executados; por isso, não há uma métrica única garantida neste README.

---

[⬆️ Voltar ao topo](#top) | [🇺🇸 Read in English](#en)

<br>

---

<a id="en"></a>

# 🇺🇸 Smartphone Replacement Prediction

A supervised machine-learning project to identify customers who are likely to replace their smartphone and predict the usage time (*aging*) associated with replacement. The workflow is implemented in Jupyter notebooks and includes exploratory analysis, model training and evaluation, as well as experiments specifically for Apple devices.

## 🚀 Goals and modeling workflow

The process has two stages:

1. **Replacement classification:** predicts the `trocou_aparelho` target.
2. **Usage-time prediction:** for customers classified as likely to replace their device, predicts `aging_aparelho`, the usage-time value/category used in the data.

The training notebooks use scikit-learn pipelines and XGBoost. The pipeline also applies SMOTE to address class imbalance. General and Apple-specific models are trained separately.

## 📂 Project structure

```text
├── ta-analysis.ipynb                 # Exploratory analysis of the general dataset
├── ta-analysis-apple.ipynb           # Exploratory analysis of the Apple dataset
├── ta-feat-imp-corr.ipynb            # Feature importance and correlation analysis
├── ta-feat-imp-corr-apple.ipynb      # Feature importance and correlations for Apple
├── ta-training-model.ipynb           # Training the general models
├── ta-training-model-apple.ipynb     # Training the Apple models
├── ta-load-model.ipynb               # Loading and evaluating the general models
├── ta-load-model-apple.ipynb         # Loading and evaluating the Apple models
├── compare-avg-pred.ipynb            # Comparing predictions on the general dataset
├── compare-avg-pred-apple.ipynb      # Comparing predictions for Apple
├── merge-all-kpi.ipynb               # Consolidating performance indicators
├── models/
│   ├── model_trocou_aparelho.pk      # General replacement propensity classifier
│   ├── model_aging.pk                # General aging classifier
│   ├── model_trocou_aparelho_apple.pk # Apple replacement propensity classifier
│   └── model_aging_apple.pk          # Apple aging classifier
└── outros_notebooks/                 # Earlier analyses and experiments
```

## 📊 Data

The datasets used by the notebooks are **not included in this repository**. The notebooks refer to external CSV files (originally configured with Kaggle paths), so update the path variables in each notebook to point to your data.

The datasets must contain the fields required by the selected workflow, including the `trocou_aparelho` and `aging_aparelho` targets and the customer/device features selected in the notebook. Apple experiments apply their own filters; review the data-preparation cells before using a different dataset.

> The data may contain customer information. Only use datasets you are authorized to access and process, in accordance with applicable privacy controls.

## 🛠️ Technologies

* Python and Jupyter Notebook
* `pandas` and `numpy` for data manipulation
* `matplotlib` and `seaborn` for visualization
* `scikit-learn`, `imbalanced-learn`, and `xgboost` for preprocessing and modeling
* `dill` for serializing trained pipelines

## ⚙️ Installation and setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate

pip install jupyter pandas numpy matplotlib seaborn scikit-learn imbalanced-learn xgboost dill scikit-plot python-dateutil
```

Launch Jupyter:

```bash
jupyter lab
```

Open the notebook you want to run and update the paths to the CSV files. Training notebooks save models under `models/`; check the serialization cells' output paths if you run a notebook from a different directory.

## ▶️ How to run

To reproduce the main workflow:

1. Run `ta-analysis.ipynb` to inspect and prepare the general data.
2. Run `ta-training-model.ipynb` to train and save the general replacement and aging classifiers.
3. Use `ta-load-model.ipynb` to load and evaluate the saved models on validation data.
4. Review `compare-avg-pred.ipynb` to compare predictions and `merge-all-kpi.ipynb` to consolidate indicators, where applicable.

For Apple-specific analysis, follow the corresponding notebooks with the `-apple` suffix.

The `.pk` files are serialized pipeline artifacts; keep dependencies and versions compatible with those used during training. Do not load serialized artifacts from untrusted sources.

## 📈 Evaluation

The notebooks include metrics and visualizations such as classification reports, confusion matrices, and ROC/AUC to evaluate the models. Results depend on the dataset, filters, and train/validation split, so this README does not claim a single guaranteed metric.

---

[⬆️ Back to top](#top) | [🇧🇷 Ler em Português](#pt-br)
