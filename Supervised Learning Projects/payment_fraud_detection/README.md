# Teste Prático de Detecção de Fraudes em Pagamentos

## 1: Conjunto de Dados
- O conjunto de dados escolhido foi o PaySim1, porém o endereço informado está incorreto, usei este (https://www.kaggle.com/code/kartik2112/fraud-detection-on-paysim-dataset)

## 2: Organização do Conjunto de Dados
- 1_infra-dataset-analysis.ipynb - Neste notebook, faço a analise dos dados do dataset, com suas devidas considerações e analises. Neste faço analises gerais das features, analise da relação entre Tipos de Transações e Valores (em geral) das transações. Respondo a algumas perguntas baseados nos dados. 

- 2_infracom-feature-importance.ipynb - Neste notebook, faço a analise de importancia das features, usando Feature Importance, Shap Values e Summary Plot, além das correlações entre as features numéricas. Uso amostragem de dados.

- 3_infracom-model-creation.ipynb - Neste notebook, cria-se o modelo de machine learning que preve o target 'isFraud', que indica se a transação é fraudulenta ou não, com avaliação de seu desempenho no conjunto de teste, utilizando métricas como precisão, recall, F1-score e matriz de confusão.

- 4_infracom-model-analysis.ipynb - Neste notebook, faço a análise e interpretação dos resultados obtidos com o modelo e as conclusões finais tanto do modelo quanto do modelo de negocio.