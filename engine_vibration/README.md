<a id="top"></a>

🌐 **Idioma / Language:** [🇧🇷 Português (PT-BR)](#pt-br) | [🇺🇸 English (EN)](#en)

---

<a id="pt-br"></a>

# 🔧 Análise de Vibração de Motores — Estudo de caso de Ciência de Dados

Projeto exploratório possui um notebook que reúne dados de vibração de acelerômetros e informações de ativos industriais para explorar sinais, relacionar sensores a equipamentos e investigar aplicações de manutenção preditiva.

> **Escopo atual:** o notebook apresenta a leitura e visualização de coletas no tempo e a exploração/junção dos dados de coletas e ativos. FFT, filtragem, cálculo de uptime/downtime e detecção automática de falhas são objetivos propostos no desafio, mas não estão implementados como soluções completas nesta versão.

## 🎯 Objetivos do desafio

* **ETL e exploração:** carregar, organizar e explorar os dados das coletas.
* **Análise de sinais:** visualizar a aceleração nos eixos X, Y e Z; investigar a representação em frequência, filtros e identificação de picos/harmônicos.
* **Contexto dos ativos:** relacionar as coletas aos ativos e às especificações dos equipamentos.
* **Manutenção preditiva:** propor métodos para estimar uptime/downtime, detectar mudanças nos padrões de vibração e identificar falhas automaticamente.
* **Conceitos de ciência de dados:** discutir viés de seleção, análise de poder, qualidade dos dados e escolha do número de clusters.

## 📂 Estrutura do projeto

```text
.
├── Tractian.ipynb                    # Notebook com a exploração e as etapas do desafio
├── 1623535615-3006-IAJ9206.csv       # Coleta de vibração bruta (eixos x, y e z)
├── 1624040490-2957-NAI1549.csv       # Coleta de vibração bruta (eixos x, y e z)
├── 1624374799-3006-MYS2071.csv       # Coleta de vibração bruta (eixos x, y e z)
├── 1624962426-3006-NAH4736.csv       # Coleta de vibração bruta (eixos x, y e z)
├── collects.csv                      # Métricas e metadados das coletas
├── assets.csv                        # Cadastro e especificações dos ativos
├── part_1.zip                        # Arquivos compactados da primeira parte
├── part_2.zip                        # Arquivos compactados da segunda parte
└── link.txt                          # Links de referência do desafio
```

## 📊 Dados

| Arquivo | Conteúdo |
| :--- | :--- |
| `1623535615-3006-IAJ9206.csv` e demais arquivos com o mesmo padrão | Amostras de aceleração em `g` nos eixos `x`, `y` e `z`. O nome identifica o início da coleta (epoch Unix), sua duração em milissegundos e o sensor. |
| `collects.csv` | Registros de coleta, incluindo sensor, duração, taxa de amostragem, temperatura e métricas RMS de aceleração e velocidade. |
| `assets.csv` | Cadastro dos ativos, sensores associados e especificações do equipamento. |

O notebook contém células que associam as coletas aos ativos pelo identificador do sensor (`sensorId`/`sensors`).

## 🧰 Tecnologias

* Python
* Jupyter Notebook / Google Colab
* pandas e NumPy para manipulação de dados
* Matplotlib para visualização

## ⚙️ Como executar

### Google Colab

1. Abra o [notebook no Google Colab](https://colab.research.google.com/drive/1Ek9RkUOpCQ03TUhzqFvcGK7SsdT3YBuB).
2. Disponibilize os arquivos de dados no Google Drive, conforme os caminhos usados no notebook.
3. Execute as células em ordem.

O notebook foi originalmente preparado para o Colab: ele monta o Google Drive e contém caminhos de diretório específicos desse ambiente.

### Execução local

1. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   # Windows: .venv\Scripts\activate
   ```

2. Instale as bibliotecas utilizadas:

   ```bash
   pip install jupyter pandas numpy matplotlib
   ```

3. Abra o notebook:

   ```bash
   jupyter notebook Tractian.ipynb
   ```

4. Antes de executar localmente, remova ou adapte a célula que importa `google.colab`/monta o Drive e atualize os comandos `os.chdir(...)` para apontarem para os diretórios locais dos CSVs.

## 🔗 Referências

* [Notebook original no Google Colab](https://colab.research.google.com/drive/1Ek9RkUOpCQ03TUhzqFvcGK7SsdT3YBuB)
* [Pasta de dados do desafio](https://drive.google.com/drive/folders/1wDi2LhO9TibEq9t-GWSE9S41Swb7oE5J)

<br>

[⬆️ Voltar ao topo](#top) | [🇺🇸 Read in English](#en)

---

<a id="en"></a>

# 🔧 Engine Vibration Analysis — Data Science Challenge

An exploratory project based on a Tractian data science challenge. The notebook brings together accelerometer vibration data and industrial asset information to explore signals, associate sensors with equipment, and investigate predictive-maintenance applications.

> **Current scope:** the notebook covers reading and visualizing vibration measurements in the time domain, as well as exploring and joining the collection and asset data. FFT, filtering, uptime/downtime calculation, and automatic fault detection are challenge objectives, but are not implemented as complete solutions in this version.

## 🎯 Challenge objectives

* **ETL and exploration:** load, organize, and explore the collection data.
* **Signal analysis:** visualize acceleration on the X, Y, and Z axes; investigate frequency-domain representation, filtering, and peak/harmonic detection.
* **Asset context:** associate measurements with assets and equipment specifications.
* **Predictive maintenance:** propose methods to estimate uptime/downtime, detect changes in vibration patterns, and identify faults automatically.
* **Data science concepts:** discuss selection bias, power analysis, data quality, and how to choose the number of clusters.

## 📂 Project structure

```text
.
├── Tractian.ipynb                    # Notebook with the exploration and challenge steps
├── 1623535615-3006-IAJ9206.csv       # Raw vibration collection (x, y, and z axes)
├── 1624040490-2957-NAI1549.csv       # Raw vibration collection (x, y, and z axes)
├── 1624374799-3006-MYS2071.csv       # Raw vibration collection (x, y, and z axes)
├── 1624962426-3006-NAH4736.csv       # Raw vibration collection (x, y, and z axes)
├── collects.csv                      # Collection metrics and metadata
├── assets.csv                        # Asset registry and specifications
├── part_1.zip                        # Compressed files for part one
├── part_2.zip                        # Compressed files for part two
└── link.txt                          # Challenge reference links
```

## 📊 Data

| File | Contents |
| :--- | :--- |
| `1623535615-3006-IAJ9206.csv` and files following the same pattern | Acceleration samples in `g` on the `x`, `y`, and `z` axes. The filename identifies the collection start (Unix epoch), duration in milliseconds, and sensor. |
| `collects.csv` | Collection records, including sensor, duration, sampling rate, temperature, and acceleration/velocity RMS metrics. |
| `assets.csv` | Asset registry, associated sensors, and equipment specifications. |

The notebook includes cells that associate collections with assets using the sensor identifier (`sensorId`/`sensors`).

## 🧰 Technologies

* Python
* Jupyter Notebook / Google Colab
* pandas and NumPy for data manipulation
* Matplotlib for visualization

## ⚙️ How to run

### Google Colab

1. Open the [notebook in Google Colab](https://colab.research.google.com/drive/1Ek9RkUOpCQ03TUhzqFvcGK7SsdT3YBuB).
2. Make the data files available in Google Drive, following the paths used in the notebook.
3. Run the cells in order.

The notebook was originally prepared for Colab: it mounts Google Drive and contains directory paths specific to that environment.

### Run locally

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   # Windows: .venv\Scripts\activate
   ```

2. Install the libraries used by the notebook:

   ```bash
   pip install jupyter pandas numpy matplotlib
   ```

3. Open the notebook:

   ```bash
   jupyter notebook Tractian.ipynb
   ```

4. Before running locally, remove or adapt the cell that imports `google.colab`/mounts Drive and update the `os.chdir(...)` commands to point to the local CSV directories.

## 🔗 References

* [Original notebook in Google Colab](https://colab.research.google.com/drive/1Ek9RkUOpCQ03TUhzqFvcGK7SsdT3YBuB)
* [Challenge data folder](https://drive.google.com/drive/folders/1wDi2LhO9TibEq9t-GWSE9S41Swb7oE5J)

<br>

[⬆️ Back to top](#top) | [🇧🇷 Ler em Português](#pt-br)
