<a id="top"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

---

<a id="pt-br"></a>

# 🇧🇷 Análise de Risco de Barragens e Predição Baseada em Dados Públicos

Este projeto tem como objetivo explorar, limpar e modelar dados públicos sobre barragens brasileiras com foco em risco, dano potencial associado e classificação da estrutura. A análise combina dados de cadastro de barragens da ANM com informações demográficas e geográficas, além de aplicar técnicas de pré-processamento e modelagem preditiva para gerar uma base de saída estruturada.

---

## 🚀 Objetivo do Projeto

O conjunto de dados foi utilizado para:

* avaliar inconsistências e valores ausentes nas informações de barragens;
* transformar variáveis textuais e numéricas em formato adequado para modelagem;
* desenvolver uma abordagem de classificação e predição de risco;
* analisar padrões por estado, município e categoria da barragem;
* gerar um arquivo de submissão com os resultados previstos.

A estrutura do trabalho está alinhada a um processo típico de ciência de dados: tratamento de dados, engenharia de atributos, modelagem preditiva e apresentação dos resultados.

---

## 📊 Fonte de Dados

Os dados utilizados neste projeto foram obtidos a partir de bases públicas relacionadas a barragens e contexto demográfico no Brasil, com destaque para:

* ANM (Agência Nacional de Mineração): informações sobre barragens e dados de cadastro;
* IBGE (Censo 2017): indicadores demográficos e urbanos;
* conjunto de dados no Kaggle sobre barragens brasileiras e domicílios de Brumadinho.

Referência principal:

* https://www.kaggle.com/edumagalhaes/brazilian-dams-and-brumadinho-households

---

## 📁 Estrutura do Repositório

```text
avalanche_prediction/
├── BeloHorizonte_Meteorological_DaliyData_from_2015until2019_versao_01.csv
├── BeloHorizonte_Meteorological_data_from_2015until2019.csv
├── IBGE_3109006_Censo2017_Brumadinho_domicilios.csv
├── IBGE_3140159_Censo2017_Mariocampos_domicilios.csv
├── IBGE_3152006_Censo2017_Pompeu_domicilios.csv
├── IBGE_3162922_Censo2017_Sao_JoaquimdasBicas_domicilios.csv
├── database_versao_LatLongDecimal_fonteANM_23_01_2019.csv
├── exercicio.py
├── submission.csv
├── verificar.txt
├── brumadinho.pdf
├── brumadinho.pptx
├── brazilian-dams-and-brumadinho-households.zip
├── README.md
└── ...
```

---

## 🧠 O que foi implementado

No script principal (`exercicio.py`) foram realizadas as seguintes etapas:

* leitura da base principal em CSV;
* verificação de valores nulos e dados inválidos;
* limpeza e conversão de colunas como `ALTURA_ATUAL_metros` e `VOLUME_ATUAL_m3`;
* imputação de valores ausentes em colunas selecionadas;
* codificação de variáveis categóricas com `pd.get_dummies()`;
* particionamento em treino e teste;
* treinamento de modelo preditivo com `RandomForestRegressor` em pipeline;
* validação cruzada e cálculo de importância de variáveis;
* geração de previsões para os atributos alvo:
  * `CATEGORIA_DE_RISCO`
  * `DANO_POTENCIAL_ASSOCIADO`
  * `CLASSE`
* exportação dos resultados em `submission.csv`.

---

## 🔎 Principais variáveis analisadas

Algumas das colunas mais importantes da base incluem:

* `NOME_BARRAGEM_MINERACAO`
* `NOME_DO_EMPREENDEDOR`
* `UF`
* `MUNICIPIO`
* `MINERIO_PRINCIPAL`
* `ALTURA_ATUAL_metros`
* `VOLUME_ATUAL_m3`
* `CATEGORIA_DE_RISCO`
* `DANO_POTENCIAL_ASSOCIADO`
* `CLASSE`
* `LATITUDE`
* `LONGITUDE`

Essas variáveis permitem tanto uma análise exploratória quanto a construção de modelos orientados a risco e classificação estrutural.

---

## 🛠️ Requisitos

É necessário ter o Python 3.9+ instalado.

Bibliotecas principais:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

## ▶️ Como executar

Na raiz do projeto, execute:

```bash
python exercicio.py
```

Esse script:

1. carrega os dados;
2. faz a limpeza e transformação dos campos;
3. treina o modelo;
4. gera gráficos de análise exploratória; e
5. salva o resultado em `submission.csv`.

---

## 📈 Resultados esperados

Ao executar o projeto, é possível observar:

* contagem de valores ausentes por coluna;
* análise de risco por categoria;
* representação de dano potencial associado;
* distribuição de classes das barragens;
* comparação por estado e município;
* arquivo final de submissão com predições estruturadas.

---

## 🧾 Observações

Este repositório representa um exercício de análise e modelagem de dados orientado a risco de barragens. O foco principal é demonstrar capacidade de:

* análise crítica dos dados;
* tratamento de inconsistências;
* pré-processamento e engenharia de atributos;
* aplicação de modelos estatísticos e preditivos;
* visualização e comunicação dos achados.

---

[⬆️ Voltar ao topo](#top) | [🇺🇸 Read in English](#en)

---

<br>

<a id="en"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

# 🇺🇸 Mining Dam Risk Analysis and Prediction Based on Public Data

This project aims to explore, clean, and model public data on Brazilian dams with a focus on risk, associated potential damage, and structural classification. The analysis combines ANM dam registry data with demographic and geographic information and applies preprocessing and predictive modeling techniques to generate a structured output dataset.

---

## 🚀 Project Goal

The dataset was used to:

* evaluate inconsistencies and missing values in dam information;
* transform textual and numerical variables into a model-ready format;
* develop a risk classification and prediction approach;
* analyze patterns by state, municipality, and dam category;
* generate a submission file with the estimated outputs.

The project follows a typical data science workflow: data cleaning, feature engineering, predictive modeling, and result presentation.

---

## 📊 Data Sources

The data used in this project comes from public Brazilian sources related to mining dams and socioeconomic context, including:

* ANM (National Mining Agency): dam registry and structural information;
* IBGE (2017 Census): demographic and urban indicators;
* Kaggle dataset on Brazilian dams and Brumadinho households.

Main reference:

* https://www.kaggle.com/edumagalhaes/brazilian-dams-and-brumadinho-households

---

## 📁 Repository Structure

```text
avalanche_prediction/
├── BeloHorizonte_Meteorological_DaliyData_from_2015until2019_versao_01.csv
├── BeloHorizonte_Meteorological_data_from_2015until2019.csv
├── IBGE_3109006_Censo2017_Brumadinho_domicilios.csv
├── IBGE_3140159_Censo2017_Mariocampos_domicilios.csv
├── IBGE_3152006_Censo2017_Pompeu_domicilios.csv
├── IBGE_3162922_Censo2017_Sao_JoaquimdasBicas_domicilios.csv
├── database_versao_LatLongDecimal_fonteANM_23_01_2019.csv
├── exercicio.py
├── submission.csv
├── verificar.txt
├── brumadinho.pdf
├── brumadinho.pptx
├── brazilian-dams-and-brumadinho-households.zip
├── README.md
└── ...
```

---

## 🧠 What was implemented

In the main script (`exercicio.py`), the following steps were performed:

* loading the main CSV dataset;
* checking null and invalid values;
* cleaning and converting columns such as `ALTURA_ATUAL_metros` and `VOLUME_ATUAL_m3`;
* imputing missing values in selected columns;
* encoding categorical variables via `pd.get_dummies()`;
* splitting train and test sets;
* training a predictive model using `RandomForestRegressor` in a pipeline;
* cross-validation and variable importance analysis;
* generating predictions for the target attributes:
  * `CATEGORIA_DE_RISCO`
  * `DANO_POTENCIAL_ASSOCIADO`
  * `CLASSE`
* exporting the results to `submission.csv`.

---

## 🔎 Key variables analyzed

Some of the most relevant columns include:

* `NOME_BARRAGEM_MINERACAO`
* `NOME_DO_EMPREENDEDOR`
* `UF`
* `MUNICIPIO`
* `MINERIO_PRINCIPAL`
* `ALTURA_ATUAL_metros`
* `VOLUME_ATUAL_m3`
* `CATEGORIA_DE_RISCO`
* `DANO_POTENCIAL_ASSOCIADO`
* `CLASSE`
* `LATITUDE`
* `LONGITUDE`

These variables support both exploratory analysis and the construction of risk- and classification-oriented models.

---

## 🛠️ Requirements

Python 3.9+ is required.

Main libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

## ▶️ How to run

From the project root, run:

```bash
python exercicio.py
```

This script:

1. loads the dataset;
2. cleans and transforms the fields;
3. trains the model;
4. generates exploratory charts; and
5. saves the output to `submission.csv`.

---

## 📈 Expected results

Running the project enables the user to observe:

* missing-value counts by column;
* risk analysis by category;
* associated damage distribution;
* dam class distribution;
* comparisons by state and municipality;
* a final submission file with structured predictions.

---

## 🧾 Notes

This repository represents a data analysis and modeling exercise focused on mining-dam risk. The main objective is to demonstrate the ability to:

* critically analyze data;
* treat inconsistencies;
* perform preprocessing and feature engineering;
* apply statistical and predictive models;
* visualize and communicate findings.

---

[⬆️ Back to top](#top) | [🇧🇷 Ler em Português](#pt-br)
