# Estimativa do custo anual de planos de saúde

## Contexto e objetivo

Uma administradora de planos de saúde quer estimar o custo anual de cada cliente a partir de informações cadastrais. O objetivo deste projeto é desenvolver e avaliar um modelo de regressão que estime esse custo e apresentar os resultados de forma útil para validação pelas áreas de negócio.

## Dados

Os arquivos do case estão na pasta [`base/`](<base/>):

- [`Seguro Saúde - Modelagem.xlsx`](<base/Seguro Saúde - Modelagem.xlsx>): dados para desenvolvimento do modelo, na planilha `MODELAGEM`, e dicionário de variáveis, na planilha `DICIONÁRIO`.
- [`Seguro Saúde - Teste Final.xlsx`](<base/Seguro Saúde - Teste Final.xlsx>): base de avaliação com a variável resposta preenchida, na planilha `Gabarito`.

O estudo considera a base de modelagem como aproximadamente 90,51% dos dados e a base de teste final como os 9,49% restantes, conforme descrito no notebook.

### Variáveis utilizadas

O notebook principal seleciona as seguintes variáveis preditoras:

| Variável | Descrição |
| --- | --- |
| `IDADE` | Idade do cliente |
| `IMC` | Índice de massa corporal |
| `FILHOS` | Quantidade de filhos |
| `FUMANTE` | Indicação se o cliente é fumante |

A variável resposta é `VALOR`, que representa o custo anual a ser estimado.

## Etapas do projeto

1. **Preparação dos dados:** leitura das planilhas, inspeção de tipos e valores ausentes e seleção das variáveis preditoras e da variável resposta.
2. **Análise exploratória:** exploração das distribuições e relações entre as variáveis para compreender os dados antes da modelagem.
3. **Pré-processamento:** padronização das variáveis numéricas, codificação one-hot das variáveis categóricas e imputação com `KNNImputer`, organizados em um pipeline.
4. **Modelagem:** treinamento de um `GradientBoostingRegressor`, com `random_state=2048`.
5. **Avaliação:** validação cruzada com cinco folds e avaliação na base de validação e na base de teste final usando R², erro médio absoluto (MAE) e erro médio quadrático (MSE).
6. **Comunicação:** apresentação dos resultados e do processo analítico no arquivo [`apresentacao.pptx`](<apresentacao.pptx>).

Na divisão usada pelo notebook principal, `train_test_split` reserva 70% da base de modelagem para validação e 30% para treinamento. A base de teste final é avaliada separadamente e contém valores conhecidos de `VALOR`.

## Arquivos do projeto

- [`prova-accenture.ipynb`](<prova-accenture.ipynb>): notebook principal, com preparação, pipeline de modelagem e avaliação.
- [`prova-acc-analysis.ipynb`](<prova-acc-analysis.ipynb>): notebook de análise exploratória.
- [`prova-acc-feat-imp.ipynb`](<prova-acc-feat-imp.ipynb>): notebook complementar de análise de importância de variáveis.
- [`apresentacao.pptx`](<apresentacao.pptx>): apresentação do case.

## Como executar

1. Abra os notebooks em um ambiente Jupyter com as dependências Python usadas pelo projeto instaladas.
2. Disponibilize os arquivos Excel da pasta `base/` no ambiente.
3. Ajuste nos notebooks os caminhos de leitura dos arquivos, que atualmente apontam para diretórios de entrada do Kaggle.
4. Execute as células do notebook principal em ordem para treinar e avaliar o modelo.

Os notebooks calculam as métricas durante a execução; os valores numéricos não estão registrados neste README.
