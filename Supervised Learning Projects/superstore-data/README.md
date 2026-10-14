# Superstore Dataset - Análise de Vendas e Lucro

## Context
Este repositório contém um conjunto de dados de vendas de um superstore global com registros de pedidos entre 2011 e 2014. A base reúne informações de clientes, produtos, regiões, canais de venda, custos de envio, descontos e rentabilidade, permitindo análises de desempenho comercial, segmentação de clientes e identificação de oportunidades de lucro.

A base foi utilizada para explorar padrões de comportamento de compra, variações por mercado e região, além de investigar como fatores como desconto, categoria do produto e canal de venda impactam os resultados financeiros da operação.

## Content
O conjunto de dados inclui 51.290 registros de pedidos e 24 colunas, com informações como:

- identificação do pedido e da linha do pedido
- data do pedido e data de envio
- modo de transporte e prioridade do pedido
- cliente, segmento, cidade, estado, país, código postal e mercado
- região, categoria, subcategoria e nome do produto
- vendas, quantidade, desconto, lucro, custo de envio e prioridade da entrega

O arquivo principal do projeto é:

- `superstore_dataset2011-2015.csv` — base raw com os registros transacionais do superstore

Além disso, o diretório também contém:

- `Cientista de dados.ipynb` — notebook com exploração inicial, análise descritiva e visualizações
- `tb_pessoa_202111101232.csv` — tabela complementar relacionada à atividade de pessoas
- `tb_resultado_pessoa.csv` — dados de resultado por pessoa
- `tb_datas.csv` — tabela auxiliar de datas

A estrutura do dataset permite responder perguntas como:

- qual segmento e região geram mais receita?
- quais categorias de produto apresentam maior margem de lucro?
- como descontos influenciam a rentabilidade?
- qual canal de venda e tipo de envio apresentam melhor desempenho?

## Acknowledgements
Agradeço à comunidade de dados e ao público que disponibiliza e compartilha bases de estudo como esta. Este projeto utiliza uma base pública de referência para fins educacionais e analíticos, e serve como material de exploração em ciência de dados, visualização e modelagem preditiva.

O dataset original foi obtido a partir da plataforma Kaggle, em um contexto de análise de vendas e performance comercial de retail global.

## Inspiration
Este projeto foi concebido para demonstrar como um conjunto de dados de negócios pode ser transformado em insights acionáveis. A inspiração vem da necessidade de compreender melhor o comportamento do consumidor, os padrões de demanda por região e categoria, além da relação entre volume de vendas e lucratividade.

Entre os principais questionamentos que motivam a análise estão:

- quais produtos e mercados impulsionam o crescimento das vendas?
- quais fatores mais impactam o lucro líquido?
- como otimizar mix de produtos, descontos e logística para melhorar a margem?
- como segmentar clientes e regiões para apoiar decisões de negócio com base em dados?

A base é especialmente útil para estudos de análise exploratória, dashboarding, aprendizado supervisionado e modelagem de previsão de vendas ou lucratividade.

---

## Estrutura do Repositório

```text
superstore-data/
├── README.md
├── superstore_dataset2011-2015.csv
├── Cientista de dados.ipynb
├── tb_pessoa_202111101232.csv
├── tb_resultado_pessoa.csv
├── tb_datas.csv
└── ...
```

Este README foi estruturado com base no template de dataset público, adaptado para o contexto do projeto de análise de vendas do superstore global.
