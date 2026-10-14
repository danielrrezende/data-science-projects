<a id="top"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

---

<a id="pt-br"></a>

# 🇧🇷 Classificação de Resultados de Recozimento

Projeto de **aprendizado de máquina supervisionado** para classificar resultados de processos de recozimento de aço em três categorias: **ideal**, **mediano** e **ruim**. O notebook reúne a preparação dos dados, análise exploratória, comparação de classificadores e geração de predições para a base de teste.

O recorte temporal considera somente experimentos realizados em **agosto de 2020**, conforme a tabela auxiliar `data_experimentos.csv`.

---

## 🚀 Etapas do Projeto

* **Integração e filtro temporal:** combina os dados de treino com a tabela de experimentos e mantém os registros de agosto de 2020.
* **Análise e preparação:** explora os dados, separa variáveis numéricas e categóricas, trata valores ausentes, padroniza variáveis numéricas e codifica categorias.
* **Tratamento do desbalanceamento:** utiliza SMOTE no conjunto de treino.
* **Comparação de modelos:** avalia Regressão Logística, Árvore de Decisão, Random Forest e Gradient Boosting em pipelines de pré-processamento e classificação.
* **Predição:** aplica o pipeline aos dados de teste e exporta as classes previstas em `submission_test.csv`.

---

## 📂 Estrutura do Projeto

```text
├── dataset/
│   ├── train.csv                # Dados de treino, incluindo o alvo recozimento
│   ├── test.csv                 # Registros a classificar
│   └── data_experimentos.csv    # Ano e mês associados a cada experimento
├── protiviti.ipynb              # Análise exploratória, treinamento e predição
├── count_plot.png               # Gráfico de contagem das classes
├── protiviti.pptx                # Apresentação do projeto
├── submission_test.csv           # Predições geradas para a base de teste
├── instruções.pdf                # Enunciado original do desafio
└── README.md
```

---

## 🗃️ Dados

| Arquivo | Conteúdo |
| :--- | :--- |
| `dataset/train.csv` | Atributos dos processos, classe de recozimento e identificador do experimento. |
| `dataset/test.csv` | Atributos dos processos que devem receber uma classificação; não contém a classe alvo. |
| `dataset/data_experimentos.csv` | Identificador do experimento e data de realização, usada para selecionar agosto de 2020. |
| `submission_test.csv` | Classificação prevista para os registros de teste, na coluna `recozimento`. |

O alvo é a coluna `recozimento`, com as classes `ideal`, `mediano` e `ruim`. A coluna `experimento` dos dados de treino se relaciona com `exp_id` da tabela auxiliar para aplicar o filtro temporal solicitado.

---

## 🧪 Metodologia e Resultado

O notebook divide os dados de treino em conjuntos de treino e validação, aplica o pré-processamento e compara quatro algoritmos de classificação. Também registra análises exploratórias e métricas de classificação.

**Observação sobre o resultado:** o notebook identifica a Árvore de Decisão como o melhor resultado comparativo, com F1 médio em torno de `0,72`; no entanto, a etapa final de geração de `submission_test.csv` instancia um modelo Gradient Boosting. Portanto, o modelo usado na submissão não coincide com o apontado como melhor na comparação e essa escolha deve ser revisitada antes de reutilizar o fluxo.

---

## ⚙️ Instalação

É necessário ter Python e Jupyter Notebook instalados. No terminal, instale as bibliotecas utilizadas pelo notebook:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn imbalanced-learn scikit-plot jupyter
```

---

## ▶️ Como Executar

Execute os comandos a partir da pasta `recozimento`, para que os caminhos relativos do notebook encontrem os arquivos em `dataset/`.

1. Abra o notebook:

   ```bash
   jupyter notebook protiviti.ipynb
   ```

2. Execute as células em ordem para refazer a análise, treinar os modelos e gerar o arquivo `submission_test.csv` na pasta do projeto.

---

## ⚠️ Observações

* O projeto não inclui um arquivo de dependências com versões fixadas; a compatibilidade pode variar conforme as versões instaladas.
* O notebook usa a opção `sparse` de `OneHotEncoder`, que foi substituída por `sparse_output` em versões recentes do scikit-learn. Se houver erro nessa etapa, ajuste o argumento conforme a versão instalada.
* `submission_test.csv` contém as predições já geradas e pode ser consultado sem executar novamente o notebook.

<br>

[⬆️ Voltar ao topo](#top) | [🇺🇸 Read in English](#en)

<br>

---

<br>

<a id="en"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

# 🇺🇸 Annealing Outcome Classification

This project uses **supervised machine learning** to classify steel annealing process outcomes into three categories: **ideal**, **mediano** (medium), and **ruim** (poor). The notebook covers data preparation, exploratory analysis, classifier comparison, and predictions for the test dataset.

Only experiments conducted in **August 2020** are included, based on the auxiliary `data_experimentos.csv` table.

---

## 🚀 Project Workflow

* **Data integration and time filter:** joins the training data with the experiment table and keeps records from August 2020.
* **Analysis and preparation:** explores the data, separates numeric and categorical features, handles missing values, scales numeric features, and encodes categories.
* **Class imbalance handling:** applies SMOTE to the training set.
* **Model comparison:** evaluates Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting using preprocessing and classification pipelines.
* **Prediction:** applies a pipeline to the test data and writes the predicted classes to `submission_test.csv`.

---

## 📂 Project Structure

```text
├── dataset/
│   ├── train.csv                # Training data, including the recozimento target
│   ├── test.csv                 # Records to classify
│   └── data_experimentos.csv    # Year and month for each experiment
├── protiviti.ipynb              # Exploratory analysis, training, and prediction
├── count_plot.png               # Class count chart
├── protiviti.pptx                # Project presentation
├── submission_test.csv           # Predictions generated for the test data
├── instruções.pdf                # Original challenge brief
└── README.md
```

---

## 🗃️ Data

| File | Contents |
| :--- | :--- |
| `dataset/train.csv` | Process features, annealing outcome, and experiment identifier. |
| `dataset/test.csv` | Process features to classify; it does not contain the target outcome. |
| `dataset/data_experimentos.csv` | Experiment identifier and date, used to select August 2020. |
| `submission_test.csv` | Predicted classifications for test records, in the `recozimento` column. |

The target is the `recozimento` column, with classes `ideal`, `mediano`, and `ruim`. The training data's `experimento` field is matched to `exp_id` in the auxiliary table to apply the required date filter.

---

## 🧪 Methodology and Result

The notebook splits the training data into training and validation sets, applies preprocessing, and compares four classification algorithms. It also contains exploratory analyses and classification metrics.

**Result note:** the notebook identifies the Decision Tree as the best model in its comparison, with an average F1 score of about `0.72`; however, the final step that generates `submission_test.csv` instantiates a Gradient Boosting model. The model used for the submission therefore differs from the one reported as best in the comparison, and this choice should be revisited before reusing the workflow.

---

## ⚙️ Installation

Python and Jupyter Notebook are required. Install the libraries used by the notebook:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn imbalanced-learn scikit-plot jupyter
```

---

## ▶️ How to Run

Run the commands from the `recozimento` project directory so the notebook's relative paths resolve to the files in `dataset/`.

1. Open the notebook:

   ```bash
   jupyter notebook protiviti.ipynb
   ```

2. Run the cells in order to reproduce the analysis, train the models, and generate `submission_test.csv` in the project directory.

---

## ⚠️ Notes

* The project does not include a dependency file with pinned versions; compatibility may vary with the installed versions.
* The notebook uses the `sparse` option of `OneHotEncoder`, which was replaced by `sparse_output` in recent scikit-learn versions. If this step raises an error, update the argument to match the installed version.
* `submission_test.csv` contains the previously generated predictions and can be inspected without rerunning the notebook.

<br>

[⬆️ Back to top](#top) | [🇧🇷 Ler em Português](#pt-br)
