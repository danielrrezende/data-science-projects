# Desafio

Desenvolva um algoritmo com base em aprendizado de máquina e análise preditiva que preveja disparos verdadeiros (considerando o cenário abaixo).

## Empresa de monitoramento (cliente Segware)

toda a empresa que utiliza a plataforma desenvolvida pela Segware para tratar sinais (eventos) decorrentes de sistemas de alarmes eletrônicos (com sensores de movimento, por exemplo), câmeras e etc.

Um dos maiores causadores de custos para as empresas de monitoramento são os deslocamentos, ou seja, quando a empresa precisa enviar uma viatura (carro ou moto) até a residência ou comércio que está sendo monitorado.

Acontece que muitas vezes esses disparos são causados por cenários diversos, como: um galho de arvore balançando ao vento, tempestades, animais, ou mesmo pelo próprio cliente querendo fazer um teste para ver se a empresa de monitoramento está mesmo de olho.

Baseando-se nos arquivos train.cvs e test.cvs, desenvolva um algoritmo que preveja se o disparo é falso ou verdadeiro, indicando a precisão do resultado.

É imprescindível que sejam comentados todos os trechos relevantes do algoritmo, explicando cada função, e decisão realizada durante o processo de desenvolvimento.

### 	Dicionário de dados:
o	Código do cliente: Código único do cliente dentro do sistema;
o	Nível de risco: grau de periculosidade do local, sendo 5 o mais alto;
o	Possui servidor CFTV: indica se o cliente possui monitoramento de imagens (0: não; 1:sim);
o	Pessoa física, jurídica ou orgão público: 0 = jurídica, 1 = física, 2 = órgão público;
o	Estado, Cidade, Bairro: Localidade do cliente;
o	Data/hora: data/hora da ocorrência do evento;
o	Código do evento: código do evento enviado;
o	Confirmado: indica se houve de fato um sinistro no cliente (0: não, 1: sim). 
