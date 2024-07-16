# Manutenção Preditiva de Caso: Paper CO

## Descrição
O que se segue é um estudo de caso fictício projetado para se assemelhar vagamente ao trabalho que você pode realizar em um projeto. Ele testará sua capacidade de lidar com big data e realizar análises estatísticas/de aprendizado de máquina, bem como sua capacidade de comunicar suas descobertas e obter insights comerciais de seu trabalho técnico. Você pode realizar as análises usando qualquer linguagem computacional que desejar (incluindo pelo menos uma ferramenta diferente do Excel). Envie seu código junto com sua apresentação e o arquivo de resultados solicitado até a data acordada com a equipe de recrutamento .

## Cenário:
A Paper CO é um importante player que produz principalmente celulose fornecendo este importante material para os fabricantes de papel e para suas próprias máquinas de papel. O mercado está cada vez mais desafiador devido à queda dos preços internacionais da celulose, veja a Figura 1.

  
Figura 1 – Preço da celulose na China em RMB
(fonte: http://www.sunsirs.com/uk/prodetail-958.html )

Devido ao cenário desafiador, a Paper Co está iniciando um projeto para redução de custos em manutenção evitando a manutenção excessiva de alguns ativos específicos e mantendo a mesma disponibilidade de todo o processo. Para isso, será necessário prever falhas nos ativos selecionados.
O chefe das operações perguntou se é possível prever tais eventos e com base em suas respostas ele mudará os planos de manutenção.

## Sua missão:
Marcamos uma reunião em uma semana com o chefe de operações, na qual você apresentará suas descobertas e fornecerá recomendações sobre a alteração dos planos de manutenção. Tanto quanto você sabe, o plano de manutenção é feito com frequência fixa por tempo de calendário. (Espera-se uma apresentação simples de suas descobertas)
A primeira fase é verificar a viabilidade de um RUL (vida útil restante) e/ou um modelo para prever a falha com pelo menos 20 ciclos de antecedência. Para treinar seu modelo, você receberá um conjunto de dados com informações de 100 eventos de falhas nesses ativos. Consulte a Tabela 1 com as informações disponíveis. Na reunião também é necessário demonstrar seu entendimento do problema e mostrar algumas estatísticas dos ativos para ilustrar o problema e a solução proposta.
Usando o modelo treinado, você deve pontuar para cada ID de ativo nos dados de teste, fornecendo as informações se o ativo falhará após mais 20 ciclos (probabilidade 0-1) ou (de preferência) quantos ciclos restantes o ativo ainda possui (RUL). Você enviará a saída do arquivo de teste que deve conter uma única coluna e uma linha para cada ativo (100 no total) fornecendo as informações acima.
Sua previsão será pontuada usando KPIs de qualidade para algoritmos de aprendizado de máquina, esteja preparado para comentar os KPIs durante a entrevista. Você pode simular cenários para demonstrar o desempenho do modelo em relação a um processo ingênuo de alteração do ativo em um período fixo.
Por fim, você terá que responder como a equipe de manutenção usará seu modelo para reduzir custos.

## Artefato 1: conjunto de dados de treinamento e teste
 
Tabela 1: Conjunto de dados com informações de falhas para cada id de ativo.
Nome do campo	Descrição
ID do recurso	Código do ativo. O código representa uma execução completa do ativo até sua falha. Após sua falha, é substituído por outro ativo com id + 1 código
tempo de execução	Uma medida de tempo que redefine após a falha
Configuração1	Definir ponto 1
Configuração2	Ponto de ajuste 2
Configuração3	Definir ponto 3
Tag1	Sensor 1
Etiqueta2	Sensor 2
…	…
Tag21	Sensor 3

