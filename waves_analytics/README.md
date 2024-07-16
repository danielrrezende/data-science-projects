# Storytelling

## 1 - Apresentação do Desafio

O desafio consiste em analisar os dados da Open Ocean Data do the Ireland's Digital Ocean Institute e fazer previsão da temperatura do mar ao longo do tempo.

## 2 - Analise e desenvolvimento do Desafio

Estes foram gerados e desenvolvidos no Microsoft Azure Databricks, ferramenta que da agilidade com varias bases de dados e manipulação dos dados

## 3 - Linguagem usada no desafio

Para tal, Foi usada:\
**Pyspark** na Coleta, Limpeza e Manipulação dos dados (notebook 1_coleta_limpa_dados) e \  
**Python** na exploração de dados na respostas das perguntas (2_explora_dados, 3_perguntas, 4_bonus)

## 4 - Distribuição das tarefas em notebooks

Para tal desafio, foram feitas, nos respectivos notebooks: \
**1_coleta_limpa_dados** - Coleta, Limpeza e Manipulação dos dados, \
**2_explora_dados** - Exploração dos dados, \
**3_perguntas** - Respostas das perguntas 'Minimum requirements' \
**4_bonus** - Analise dos dados da time series E criação do modelo de time series

## 5 - Perguntas do desafio

1) Na **primeira questão**, listei as menores temperaturas lidas pelas boias, e identifiquei estas no mapa do pais. A principio eu também estava listando as bays, posteriormente percebi que o enunciado só pedia pelos Buoy. Também informei, através de um gráfico de pizza, quais os meses de maior ocorrencia.\

![image](https://user-images.githubusercontent.com/43621929/192382101-afe00136-79c4-4d83-9450-b2bb6f51e5b9.png)

Localização das Boias (Bouys) que registraram menores temperaturas\
![image](https://user-images.githubusercontent.com/43621929/192382152-6358dfd0-d0bf-49da-a46c-c3531318bda0.png)


Which usually month it occurs?\
![image](https://user-images.githubusercontent.com/43621929/192382279-9da3d277-02ca-41aa-a4a0-c037634c711d.png)


\
2) Na **segunda questão**, listei o local de maior nivel de água, indicando também no mapa. Foi indicado o mês de ocorrencia.\
![image](https://user-images.githubusercontent.com/43621929/192382396-9afda6d4-9951-4b2c-895c-dd8eb639bacc.png)

Localização no mapa\
![image](https://user-images.githubusercontent.com/43621929/192382429-8361efb9-09f4-4ac0-a582-54100d60032f.png)

Which usually month it occurs?\
![image](https://user-images.githubusercontent.com/43621929/192382596-9d0d0042-c26d-4755-8fa3-3711eb9e764b.png)



\
3) Na **terceira questão**, fiz uma correlação entre as features **Wave Lenghts (Hmax)** com **Sea Temperature** e vi que possuem correlação negativa de -0,29, o que indica que uma leve influencia entre as features (valor 0,29, que vai de 0 a 1), e pelo fato de ser negativa, indica que uma feature pode ter influencia contraria sobre a outra.\
![image](https://user-images.githubusercontent.com/43621929/192382807-949092ed-a7d3-4f23-bf2e-4eef72e8543b.png)

Com relação a **latitude** e **longitude**, possuem correlação em modulo de -0,033 e 0,08 respectivamente, bem proximas de 0, o que indica que não se sabe exatamente o que ocorre com uma feature quando a outra varia e portanto, pode indicar uma potencial complementariedade entre si, sendo potenciais candidatas à combinação de features\

![image](https://user-images.githubusercontent.com/43621929/192382842-4e46839a-e45d-4a92-9216-b7b709909fff.png)


## 6 - Lidando o desafio

1) Primeiramente:
- fiz a **análise da feature de tempo**, que vai de **2021-09-20 a 2022-09-21**\

- depois **Análise de target da série temporal**, no caso SeaTemperature, vi que para um mesmo dia, existe casos de varias medições. Para lidar com isso, fiz uma media de temperatura para um dado dia, com todas as medições deste dia. Verifiquei o número de valores ausentes na coluna de destino.\
![image](https://user-images.githubusercontent.com/43621929/192383039-42db59ae-a2ff-4236-bd6d-34ea8091194d.png)


- Visualizei os dados\
![image](https://user-images.githubusercontent.com/43621929/192383128-2fe497d8-ecbd-4c5f-a96e-c82de9a3ff39.png)


2)Na montagem do modelo, fiz visualizações sazonais ao longo de uma semana e mais de um ano\
![image](https://user-images.githubusercontent.com/43621929/192383222-3c5d1930-2bc4-43eb-a66f-8edd7713beca.png)


- analise Periodograma, ou seja, por periodos de tempo\
![image](https://user-images.githubusercontent.com/43621929/192383262-9cf8dc27-b531-4725-ad24-5e6815981b3d.png)


- Uso de DeterministicProcess, usado para criar recursos de tendência
Finalmente, Sea Temperature - Seasonal Forecast, previsões de temperatura do mar, para um periodo de 1 ano

![image](https://user-images.githubusercontent.com/43621929/192383329-3b356a56-1863-4a0a-8b25-8d03760b85ce.png)



