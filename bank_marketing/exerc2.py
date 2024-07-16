# 2. Fazendo uma relação entre número de contatos e sucesso da campanha quais
# são os pontos relevantes a serem observados?

import numpy as np
import pandas as pd

# import csv file
bank = pd.read_csv("bank-full.csv", sep=';')

# set and load variables
campaign = np.array(bank['campaign'])               # número de contatos realizados durante esta campanha e para este cliente
future_client = np.array(bank['y'])                 # número de clientes que assinaram um depósito a prazo
salarios = np.array(bank['balance'])                # media de salario total
marital = np.array(bank['marital'])                 # estado civil

#======================================================================= estado civil
#"marital" and yes
marital_y = marital[future_client == 'yes']
#"marital" and no
marital_n = marital[future_client == 'no']

#total married
total_married = marital[marital == 'married']
#"married" and yes
married_y = marital_y[marital_y == 'married']
#"married" and no
married_n = marital_n[marital_n == 'married']

#total divorced
total_divorced = marital[marital == 'divorced']
#"divorced" and yes
divorced_y = marital_y[marital_y == 'divorced']
#"divorced" and no
divorced_n = marital_n[marital_n == 'divorced']

#total single
total_single = marital[marital == 'single']
#"single" and yes
single_y = marital_y[marital_y == 'single']
#"single" and no
single_n = marital_n[marital_n == 'single']
#======================================================================= salarios
# salarios de quem assinou e quem nao assinou
salarios_subscribed = salarios[future_client == 'yes']
salarios_unsubscribed = salarios[future_client == 'no']

# media de salario de quem assinou e media de quem não assinou
media_salario_subscribed = np.mean(salarios_subscribed)
media_salario_unsubscribed = np.mean(salarios_unsubscribed)

#======================================================================= selecionando clientes
# selecionando clientes que assinaram e os que não
client_subscribed = future_client[future_client == 'yes']
client_unsubscribed = future_client[future_client == 'no']
##print('#============================================= CLASSIFICAÇÃO GERAL =========================================')
##print("O numero de clientes que assinaram é %i" %(len(client_subscribed)))
##print("O numero de clientes que não assinaram é %i" %(len(client_unsubscribed)))

#======================================================================= contatos
# media e total de contatos
total_call = sum(campaign)
mean_campaign = np.mean(campaign)
##print("O número total de ligações foi %i" %total_call)
##print("O numero médio de contatos foi de : %i" %mean_campaign)

print("#============================================= RESPOSTA ===================================================")
# conclusão, proporção entre numero de ligações e clientes que assinaram
print("")
print('#============================================= PROPORÇÃO ====================================================')
proporcao = total_call / len(client_subscribed)
proporcao = int(proporcao)
print("A conclusão é que para cada aproximadamente %i" %proporcao + " clientes contactados, 1 adere a campanha, ou seja, %.2f"  %((len(client_subscribed)*100)/total_call) + "%")
print("")

print('#============================================= MEDIA SALARIAL ===============================================')
# analisar media salarial dos que assinaram a campanha e dos que não assinaram a campanha
##neste caso concluir se as pessoas assinaram a campanha por necessidade pelo fato de ganharaem pouco
##ou se tiver mais pessoas que ganham mais pelo fato de terem mais credito disponivel pela alta renda
## fazer relação entre media de quem assinou e media de quem não assinou
print("A media de salário de quem assinou a campanha é de EU %i" %media_salario_subscribed + " e a media dos que NÃO assinaram a campanha é de EU %i" %media_salario_unsubscribed)
if (int(media_salario_subscribed)) > (int(media_salario_unsubscribed)):
    print("A media de salário dos que assinaram a campanha é MAIOR do que os que não assinaram")
else:
    print("A media de salário dos que assinaram a campanha é MENOR do que os que não assinaram")

print("")

print('#============================= ENTRE CASADOS, DIVORCIADOS E SOLTEIROS ====================================')
# pode se analisar também estado civil e educação
##neste caso pode se concluir que pessoas casadas teoricamente precisam de mais dinheiro
porc_married = int(((len(married_y)*100)/len(total_married)))
porc_divorced = int(((len(divorced_y)*100)/len(total_divorced)))
porc_single = int(((len(single_y)*100)/len(total_single)))
print("Total de Casados é de " + str(len(total_married)) + ", sendo que " + str(len(married_y)) + " aderiram a campanha e " + str(len(married_n)) + " NÃO aderiram, ou seja, %.2f"  %porc_married + "%")
print("Total de Divorciados é de " + str(len(total_divorced)) + ", sendo que " + str(len(divorced_y)) + " aderiram a campanha e " + str(len(divorced_n)) + " NÃO aderiram, ou seja, %.2f"  %porc_divorced + "%")
print("Total de Solteiros é de " + str(len(total_single)) + ", sendo que " + str(len(single_y)) + " aderiram a campanha e " + str(len(single_n)) + " NÃO aderiram, ou seja, %.2f" %porc_single + "%")
if ((porc_married > porc_divorced) & (porc_married > porc_single)):
    print("Casados aderem mais ao programa")
elif ((porc_divorced > porc_married) & (porc_divorced > porc_single)):
    print("Divorciados aderem mais ao programa")
else:
    print("Solteiros aderiram mais ao programa")
