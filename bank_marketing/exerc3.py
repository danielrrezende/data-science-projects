# 3. Baseando-se nos resultados de adesão desta campanha qual o número médio e
# o máximo de ligações que você indica para otimizar a adesão?

import numpy as np
import pandas as pd

# import csv file
bank = pd.read_csv("bank-full.csv", sep=';')

# set and load variables
campaign = np.array(bank['campaign'])               # número de contatos realizados durante esta campanha e para este cliente
future_client = np.array(bank['y'])                 # número de clientes que assinaram um depósito a prazo

#======================================================================= selecionando clientes
# selecionando clientes que assinaram e os que não
client_subscribed = future_client[future_client == 'yes']
client_unsubscribed = future_client[future_client == 'no']
print('#============================================= CLASSIFICAÇÃO GERAL =========================================')
print("O numero de clientes que assinaram é " + str(len(client_subscribed)))
print("O numero de clientes que não assinaram é " + str(len(client_unsubscribed)))

#======================================================================= contatos
# media e total de contatos
total_call = sum(campaign)
mean_campaign = np.mean(campaign)
print("O número total de ligações foi " + str(total_call))
print("O numero médio de contatos foi de : " + str(mean_campaign))

#========================================================================= CONCLUSÕES
# conclusão, proporção entre numero de ligações e clientes que assinaram
print("")
print('#============================================= PROPORÇÃO ====================================================')
proporcao = total_call / len(client_subscribed)
proporcao = int(proporcao)
print("A conclusão é que para cada aproximadamente " + str(proporcao) + " clientes contactados, 1 adere a campanha, ou seja, " + str(int(((len(client_subscribed)*100)/total_call))) + "%")
print("")

print('#============================================= RESPOSTA ====================================================')
print("O numero médio de contatos indicável é : " + str(int(mean_campaign)))
print("O numero máximo de contatos indicável é : " + str(int(mean_campaign)))
