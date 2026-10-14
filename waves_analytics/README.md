<a id="top"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

---

<a id="pt-br"></a>

# 🇧🇷 Waves Analytics

Projeto de análise exploratória e modelagem preditiva de dados oceânicos coletados na costa da Irlanda. O objetivo principal é entender padrões de temperatura da água, altura de onda e comportamento sazonal dos fenômenos marítimos, além de desenvolver uma previsão de séries temporais para a variável de interesse: a temperatura do mar.

---

## 🚀 Visão Geral

Este projeto combina dados de boias oceanográficas e estações de mare e onda para responder perguntas analíticas sobre:

- quais regiões registram as menores temperaturas da água;
- em que meses esses eventos ocorrem com maior frequência;
- como a altura de onda (Hmax) se relaciona com a temperatura da superfície;
- qual o comportamento sazonal e temporal da temperatura marinha;
- como construir um modelo de previsão para um horizonte de 1 ano.

Os dados foram processados em notebooks do ambiente Azure Databricks, com uso de PySpark para coleta, limpeza e manipulação inicial, e Python para exploração, visualização e modelagem estatística.

---

## 📊 Dados e Fonte do Projeto

A base de dados é composta por séries temporais de observações marinhas, com foco em:

- ondas: `wave/`
- marés: `tide/`
- dados consolidados e exportados: `database/export.csv`

Algumas colunas relevantes incluem:

- `time`
- `latitude` e `longitude`
- `station_id`
- `PeakPeriod`
- `SignificantWaveHeight`
- `Hmax`
- `SeaTemperature`
- `MeanCurSpeed`
- `MeanCurDirTo`

A combinação dessas variáveis permite avaliar a dinâmica oceânica em escala espacial e temporal, além de criar indicadores para modelagem preditiva.

---

## 🧭 Objetivos do Desafio

A análise foi organizada em etapas:

1. Coleta e limpeza dos dados
2. Exploração e interpretação dos padrões oceânicos
3. Resposta a perguntas de negócio e ciência de dados
4. Desenvolvimento de uma série temporal para prever temperatura do mar
5. Interpretação dos resultados e validação visual

---

## 🗂️ Estrutura do Projeto

```text
waves_analytics/
├── 1_coleta_limpa_dados.ipynb     # coleta, limpeza e preparação dos dados
├── 2_explora_dados.ipynb          # análise exploratória e visualizações
├── 3_perguntas.ipynb              # respostas às perguntas do desafio
├── 4_bonus.ipynb                 # análise da série temporal e previsão
├── dadosfera.ipynb               # notebook complementar / investigação extra
├── database/
│   ├── export.csv                # base consolidada
│   ├── tide/                     # arquivos de dados de maré
│   └── wave/                     # arquivos de dados de onda
├── tide/                         # cópias locais dos dados de maré
├── wave/                         # cópias locais dos dados de onda
├── README.md                     # documentação do projeto
└── .gitignore                    # arquivos ignorados pelo Git
```

---

## 🛠️ Tecnologias Utilizadas

- **PySpark** para coleta, limpeza e manipulação dos dados em larga escala
- **Python** para exploração, análise estatística e visualização
- **Pandas / NumPy** para preparação de dados e cálculos
- **Matplotlib / Seaborn** para visualização
- **Databricks** como ambiente principal de execução
- **Modelagem de séries temporais** com abordagem de decomposição e previsão sazonal

---

## 📈 Principais Insights da Análise

Ao longo do projeto, foram identificados e explorados diversos padrões relevantes:

- regiões com as menores temperaturas registradas pelas boias;
- meses de maior ocorrência de eventos extremos ou atípicos;
- análise espacial das medições no mapa da Irlanda;
- correlação entre a variável `Hmax` e `SeaTemperature`;
- avaliação da influência de latitude e longitude nas observações;
- decomposição temporal da série e identificação de sazonalidade;
- previsão de temperatura do mar para um horizonte anual.

A correlação entre altura máxima de onda e temperatura apresentou comportamento negativo, indicando que o aumento da amplitude das ondas pode estar associado a condições oceânicas diferentes das observações de temperatura da superfície. Esse tipo de relação ajuda a orientar análises futuras de modelagem e sensibilidade climática.

---

## 🧪 Fluxo de Trabalho do Projeto

### 1. Coleta e limpeza
A primeira etapa consistiu em carregar os dados de ondas e marés, realizar padronização de colunas, tratar valores faltantes e preparar a base para a análise.

### 2. Exploração dos dados
Os notebooks foram usados para:

- visualizar a distribuição temporal;
- comparar estações e regiões;
- identificar períodos de maior variabilidade;
- mapear ocorrências geográficas por temperatura e nível de água.

### 3. Respostas às perguntas do desafio
O projeto respondeu perguntas analíticas referentes a:

- menor temperatura observada por boia;
- mês mais frequente de ocorrência;
- maior nível de água e sua localização;
- relação entre variáveis físicas do ambiente marinho.

### 4. Modelagem de séries temporais
A etapa final focou na análise da série temporal da temperatura do mar, com:

- agregação diária da variável alvo;
- verificação de valores ausentes;
- visualização de tendência e sazonalidade;
- uso de `DeterministicProcess` e estrutura de previsão sazonal;
- previsão para um período de 1 ano.

---

## ✅ Requisitos e Execução

### Requisitos

- Python 3.10+
- Jupyter Notebook ou ambiente Databricks
- Bibliotecas principais: `pyspark`, `pandas`, `numpy`, `matplotlib`, `seaborn`

### Como executar

1. Abra o notebook `1_coleta_limpa_dados.ipynb` para preparar e limpar a base.
2. Em seguida, execute `2_explora_dados.ipynb` para validar padrões e visualizar tendências.
3. Use `3_perguntas.ipynb` para responder as perguntas do desafio.
4. Por fim, execute `4_bonus.ipynb` para realizar a análise temporal e a previsão.

> O projeto foi originalmente desenvolvido no Microsoft Azure Databricks, mas a estrutura dos notebooks permite adaptação para execução local em ambiente Python/Jupyter.

---

## 📌 Resultado Esperado

O conjunto de análises produz uma visão integrada sobre o comportamento dos dados oceânicos na região estudada, permitindo:

- localizar áreas com temperaturas mais baixas;
- relacionar fenômenos físicos e temporais;
- detectar sazonalidade e variabilidade da temperatura do mar;
- produzir previsões úteis para monitoramento ambiental e tomada de decisão.

---

## 📚 Referências

- Open Ocean Data / Ireland's Digital Ocean Institute
- Dados de boias e estações de medição oceânica
- Análise de séries temporais e previsões sazonais em contextos ambientais

---

[⬆️ Voltar ao topo](#top)

---

<a id="en"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

# 🇺🇸 Waves Analytics

A data science project focused on exploratory analysis and predictive modeling of ocean data collected along the Irish coast. The primary goal is to understand sea temperature patterns, wave behavior, and seasonal dynamics, while also developing a time-series forecast for the target variable: sea temperature.

---

## 🚀 Project Overview

This project combines wave and tide data from ocean monitoring stations to answer analytical questions such as:

- which regions show the lowest water temperatures;
- which months are most associated with those events;
- how wave height (`Hmax`) relates to sea temperature;
- how seasonal and temporal patterns evolve over time;
- how to build a forecasting model for a one-year horizon.

The data was processed in Azure Databricks notebooks, using PySpark for ingestion and cleaning and Python for exploratory analysis, visualization, and statistical modeling.

---

## 🧱 Project Structure

```text
waves_analytics/
├── 1_coleta_limpa_dados.ipynb
├── 2_explora_dados.ipynb
├── 3_perguntas.ipynb
├── 4_bonus.ipynb
├── dadosfera.ipynb
├── database/
│   ├── export.csv
│   ├── tide/
│   └── wave/
├── tide/
├── wave/
├── README.md
└── .gitignore
```

---

## 🔍 Main Analysis Topics

- spatial analysis of low-temperature measurements;
- identification of seasonal peaks and monthly concentration;
- correlation between wave conditions and sea temperature;
- time-series decomposition and trend analysis;
- seasonal forecasting of sea temperature.

---

## ⚙️ Tools and Stack

- PySpark
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Azure Databricks
- Time-series forecasting with seasonal decomposition and trend modeling

---

## ▶️ How to Run

1. Open `1_coleta_limpa_dados.ipynb` to prepare the data.
2. Run `2_explora_dados.ipynb` for exploratory analysis and charts.
3. Use `3_perguntas.ipynb` to answer challenge-specific questions.
4. Execute `4_bonus.ipynb` for the time-series forecast analysis.

---

[⬆️ Back to top](#top)
