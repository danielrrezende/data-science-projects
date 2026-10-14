<a id="top"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

---

<a id="pt-br"></a>

# 🇧🇷 Previsão de passagens em rodovias

Projeto de análise e modelagem de dados de localização para estudar a distribuição de leituras de dispositivos ao longo de trechos rodoviários. Os notebooks preparam coordenadas por quilômetro, consultam dados armazenados em MySQL, organizam as leituras em arquivos CSV e experimentam modelos de aprendizado de máquina para estimar leituras em diferentes períodos do dia.

> **Nota:** as leituras de dispositivos são usadas como sinal indireto de circulação; não devem ser interpretadas automaticamente como uma contagem oficial de veículos.

---

## 🚀 O que o projeto faz

* Prepara e converte dados geográficos de rodovias, incluindo arquivos CSV e KML.
* Consulta dados de localização e leituras em uma base MySQL.
* Consolida leituras por quilômetro e por faixas horárias de seis horas.
* Treina e avalia modelos tradicionais e redes neurais para prever essas leituras.
* Armazena conjuntos de dados processados e artefatos de modelos para análise posterior.

---

## 📂 Estrutura do projeto

```text
previsao_passagens/
├── diversos/
│   └── querys.sql                 # Consultas e comandos SQL de apoio
├── docker/                        # Configuração de contêineres do ambiente original
├── inputs/                        # Dados de entrada e coordenadas da Dutra
├── model/dutra/                   # Modelos Keras salvos (.h5)
├── notebooks/
│   ├── functions/                 # Funções auxiliares para experimentos
│   ├── ehook_data_extractor.ipynb # Preparação de coordenadas e extração de dados
│   ├── ehook_sql_extractor.ipynb  # Extração SQL de leituras por rodovia
│   ├── ehook_data_constructor.ipynb # Consolidação dos CSVs de leitura
│   ├── ehook_model.ipynb          # Experimentos com modelos scikit-learn
│   ├── ehook_model_deep_learning.ipynb # Experimentos com Keras
│   ├── db_extractor.ipynb         # Consultas exploratórias à base
│   ├── kml_reader.ipynb           # Leitura e transformação de arquivos KML
│   └── get_coordenates_google.ipynb # Geocodificação com Google Maps
├── outputs/                       # Dados intermediários e consultas da Dutra
├── outputs_2020-01-07/            # Resultados de uma execução histórica
├── outputs_2020-02-07/            # Resultados de uma execução histórica
├── outputs_2020-03-07/            # Resultados de uma execução histórica
└── README.md
```

Há notebooks adicionais em `notebooks/another_notebooks/`, voltados a explorações e experimentos anteriores.

---

## 🧭 Notebooks e fluxo de trabalho

| Etapa | Notebook / recurso | Finalidade |
| :--- | :--- | :--- |
| Coordenadas | [`kml_reader.ipynb`](notebooks/kml_reader.ipynb), [`get_coordenates_google.ipynb`](notebooks/get_coordenates_google.ipynb) | Ler ou obter coordenadas para os pontos da rodovia. |
| Extração | [`ehook_data_extractor.ipynb`](notebooks/ehook_data_extractor.ipynb), [`ehook_sql_extractor.ipynb`](notebooks/ehook_sql_extractor.ipynb) | Consultar dados MySQL e extrair leituras por quilômetro e período. |
| Exploração | [`db_extractor.ipynb`](notebooks/db_extractor.ipynb), [`db_consultant.ipynb`](notebooks/db_consultant.ipynb) | Explorar tabelas e resultados da base de dados. |
| Preparação | [`ehook_data_constructor.ipynb`](notebooks/ehook_data_constructor.ipynb) | Combinar os arquivos de leituras em uma base adequada aos experimentos. |
| Modelagem | [`ehook_model.ipynb`](notebooks/ehook_model.ipynb) | Treinar e avaliar modelos scikit-learn. |
| Deep learning | [`ehook_model_deep_learning.ipynb`](notebooks/ehook_model_deep_learning.ipynb) | Treinar, avaliar e carregar modelos Keras. |

O experimento de modelagem usa atributos relacionados à rodovia, estado e quilômetro e prevê as leituras em quatro faixas (`00–06`, `06–12`, `12–18` e `18–24`). Os notebooks permitem selecionar os períodos de treino e avaliação; confira os caminhos e parâmetros nas primeiras células antes da execução.

---

## 🗃️ Dados e resultados

* `inputs/dutra.csv` contém referências de rodovia, quilômetro e estado.
* `inputs/dutra_all.csv`, `inputs/dutra_all.kml` e arquivos relacionados fornecem dados geográficos em formatos diferentes.
* `outputs/` contém resultados intermediários, incluindo consultas de coordenadas e arquivos de leituras.
* `outputs_2020-*/dutra/` contém dados organizados por data e período, além de arquivos de previsão gerados pelos notebooks.
* `model/dutra/` contém modelos de deep learning salvos no formato HDF5 (`.h5`).

Os resultados versionados representam execuções históricas e podem não refletir uma extração atualizada da base de dados.

---

## 🛠️ Pré-requisitos

* Python 3 e Jupyter Notebook ou JupyterLab.
* MySQL acessível e os dados/tabelas esperados pelas consultas, caso vá executar os notebooks de extração.
* Dependências Python conforme os notebooks que pretende executar. Não há um arquivo `requirements.txt` ou equivalente neste projeto.
* Uma chave e acesso à API do Google Maps, caso execute o notebook de geocodificação.
* TensorFlow/Keras para os experimentos de deep learning.

Os notebooks também usam bibliotecas como `pandas`, `numpy`, `scikit-learn`, `matplotlib` e `mysql-connector-python`; os notebooks geográficos podem usar `folium`, `geopy` ou `googlemaps`.

---

## ⚙️ Instalação

Na raiz deste diretório, crie um ambiente virtual e instale Jupyter e as bibliotecas necessárias aos notebooks selecionados:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyter pandas numpy matplotlib scikit-learn mysql-connector-python
```

No Windows, ative o ambiente com:

```powershell
.venv\Scripts\Activate.ps1
```

Instale separadamente as dependências específicas que faltarem, por exemplo `tensorflow`/`keras` para deep learning ou `folium`, `geopy` e `googlemaps` para os notebooks de geolocalização. As versões não estão fixadas no repositório; a compatibilidade pode depender da versão do Python e do ambiente de execução.

---

## ▶️ Como executar

1. Abra um terminal na raiz do projeto, ative o ambiente virtual e inicie o Jupyter:

   ```bash
   jupyter lab
   ```

2. Abra os notebooks na ordem correspondente ao seu objetivo. Para refazer a preparação a partir da base, use o fluxo de coordenadas, extração, construção dos dados e modelagem.
3. Antes de executar células de banco de dados, configure localmente host, usuário, senha e nome da base conforme seu ambiente MySQL. **Não versione senhas nem chaves de API.**
4. Verifique os caminhos de entrada e saída e os valores de data/rodovia definidos nos notebooks. Vários caminhos são relativos ao diretório `notebooks/`, portanto abra e execute os arquivos mantendo a estrutura do projeto.
5. Execute as células na ordem. Os notebooks de extração gravam CSVs em `outputs/` ou em diretórios `outputs_<data>/`; os notebooks de modelo leem esses arquivos e podem gravar previsões nesses diretórios.

As consultas SQL de referência também estão em [`diversos/querys.sql`](diversos/querys.sql). Elas foram escritas para o esquema e o contexto de dados usados originalmente e podem precisar de ajustes antes de serem executadas em outra base.

---

## 🔒 Configuração de credenciais

Os notebooks de extração contêm células com parâmetros de conexão ao banco de dados. Substitua-os localmente por valores apropriados ao seu ambiente e não salve credenciais reais nos notebooks ou em commits. Para geocodificação, configure sua própria chave da API do Google Maps conforme as instruções do provedor.

---

<br>

[⬆️ Voltar ao topo](#top) | [🇺🇸 Read in English](#en)

<br>

---

<a id="en"></a>

# 🇺🇸 Highway passage prediction

This project explores location data and models device readings along highway segments. Its notebooks prepare per-kilometer coordinates, query readings stored in MySQL, organize observations into CSV files, and experiment with machine-learning models to estimate readings across different times of day.

> **Note:** device readings are an indirect signal of movement and should not automatically be treated as an official vehicle count.

---

## 🚀 What it does

* Prepares and transforms highway geospatial data, including CSV and KML files.
* Queries location and reading data from a MySQL database.
* Aggregates readings by kilometer and six-hour time windows.
* Trains and evaluates traditional machine-learning models and neural networks.
* Stores processed datasets and model artifacts for further analysis.

---

## 📂 Project structure

```text
previsao_passagens/
├── diversos/
│   └── querys.sql                   # Supporting SQL queries and commands
├── docker/                          # Container configuration from the original environment
├── inputs/                          # Input data and Dutra highway coordinates
├── model/dutra/                     # Saved Keras models (.h5)
├── notebooks/
│   ├── functions/                   # Helper functions for experiments
│   ├── ehook_data_extractor.ipynb   # Coordinate preparation and data extraction
│   ├── ehook_sql_extractor.ipynb    # SQL extraction of highway readings
│   ├── ehook_data_constructor.ipynb # CSV reading-data consolidation
│   ├── ehook_model.ipynb            # scikit-learn model experiments
│   ├── ehook_model_deep_learning.ipynb # Keras experiments
│   ├── db_extractor.ipynb           # Exploratory database queries
│   ├── kml_reader.ipynb             # KML reading and transformation
│   └── get_coordenates_google.ipynb  # Geocoding with Google Maps
├── outputs/                         # Intermediate Dutra data and query results
├── outputs_2020-01-07/              # Historical run results
├── outputs_2020-02-07/              # Historical run results
├── outputs_2020-03-07/              # Historical run results
└── README.md
```

Additional exploratory and earlier notebooks are available in `notebooks/another_notebooks/`.

---

## 🧭 Notebooks and workflow

| Stage | Notebook / resource | Purpose |
| :--- | :--- | :--- |
| Coordinates | [`kml_reader.ipynb`](notebooks/kml_reader.ipynb), [`get_coordenates_google.ipynb`](notebooks/get_coordenates_google.ipynb) | Read or obtain highway point coordinates. |
| Extraction | [`ehook_data_extractor.ipynb`](notebooks/ehook_data_extractor.ipynb), [`ehook_sql_extractor.ipynb`](notebooks/ehook_sql_extractor.ipynb) | Query MySQL and extract readings by kilometer and time period. |
| Exploration | [`db_extractor.ipynb`](notebooks/db_extractor.ipynb), [`db_consultant.ipynb`](notebooks/db_consultant.ipynb) | Explore database tables and results. |
| Preparation | [`ehook_data_constructor.ipynb`](notebooks/ehook_data_constructor.ipynb) | Combine reading files into datasets for the experiments. |
| Modeling | [`ehook_model.ipynb`](notebooks/ehook_model.ipynb) | Train and evaluate scikit-learn models. |
| Deep learning | [`ehook_model_deep_learning.ipynb`](notebooks/ehook_model_deep_learning.ipynb) | Train, evaluate, and load Keras models. |

The modeling experiments use features related to the highway, state, and kilometer, and predict readings in four time windows (`00–06`, `06–12`, `12–18`, and `18–24`). Training and evaluation periods can be selected in the notebooks; check their initial cells before running them.

---

## 🗃️ Data and results

* `inputs/dutra.csv` contains highway, kilometer, and state references.
* `inputs/dutra_all.csv`, `inputs/dutra_all.kml`, and related files provide geospatial data in different formats.
* `outputs/` contains intermediate results, including coordinate queries and reading files.
* `outputs_2020-*/dutra/` contains data organized by date and time period, as well as predictions generated by the notebooks.
* `model/dutra/` contains deep-learning models saved in HDF5 (`.h5`) format.

The committed results are historical runs and may not reflect a fresh extraction from the database.

---

## 🛠️ Requirements

* Python 3 and Jupyter Notebook or JupyterLab.
* An accessible MySQL database with the tables expected by the queries, if running the extraction notebooks.
* Python packages required by the notebooks you intend to run. This project does not include a `requirements.txt` or equivalent dependency manifest.
* A Google Maps API key and access, if running the geocoding notebook.
* TensorFlow/Keras for the deep-learning experiments.

The notebooks also use packages such as `pandas`, `numpy`, `scikit-learn`, `matplotlib`, and `mysql-connector-python`; geospatial notebooks may use `folium`, `geopy`, or `googlemaps`.

---

## ⚙️ Installation

From this directory, create a virtual environment and install Jupyter and the packages needed by the selected notebooks:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyter pandas numpy matplotlib scikit-learn mysql-connector-python
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Install any notebook-specific dependencies separately, such as `tensorflow`/`keras` for deep learning or `folium`, `geopy`, and `googlemaps` for geospatial notebooks. Package versions are not pinned in this repository; compatibility may depend on the Python version and runtime environment.

---

## ▶️ Running the project

1. Open a terminal in the project directory, activate the virtual environment, and start Jupyter:

   ```bash
   jupyter lab
   ```

2. Open the notebooks in the order appropriate to your goal. To rebuild the data from the database, follow the coordinates, extraction, data-construction, and modeling workflow.
3. Before running database cells, configure the host, username, password, and database name locally for your MySQL environment. **Do not commit passwords or API keys.**
4. Check input/output paths and the date/highway values defined in the notebooks. Several paths are relative to the `notebooks/` directory, so keep the project structure intact when opening and running the files.
5. Run the notebook cells in order. Extraction notebooks write CSVs under `outputs/` or `outputs_<date>/`; model notebooks read those files and may save predictions in the same directories.

Reference SQL queries are also available in [`diversos/querys.sql`](diversos/querys.sql). They were written for the original schema and data context and may need adjustment before being run against another database.

---

## 🔒 Credentials

Database connection parameters are present in extraction notebook cells. Replace them locally with values for your environment and do not save real credentials in notebooks or commits. For geocoding, configure your own Google Maps API key according to the provider's instructions.

<br>

[⬆️ Back to top](#top) | [🇧🇷 Ler em Português](#pt-br)
