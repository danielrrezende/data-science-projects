# 4. O resultado da campanha anterior tem relevância na campanha atual?

import numpy as np
import pandas as pd

# import csv file
bank = pd.read_csv("bank-full.csv", sep=';')

# set and load variables
campaign = np.array(bank['campaign'])   # número de contatos realizados durante esta campanha e para este cliente
future_client = np.array(bank['y'])     # número de clientes que assinaram um depósito a prazo
pdays = np.array(bank['pdays'])         # número de dias que passaram depois que o cliente foi contatado pela última vez de uma campanha anterior
previous = np.array(bank['previous'])   # número de contatos realizados antes desta campanha e para este cliente
poutcome = np.array(bank['poutcome'])   # resultado da campanha de marketing anterior

#======================================================================= se houve contato anterior e quantos dias
# pdays - se o cliente que foi contactado anteriormente ou não, pode ter influencia na campanha atual
no_contact = 0
contacts = 0
for i in pdays:
    if pdays[i] == -1:
        no_contact += 1;
    else:
        contacts += 1;
por_contacts = ((no_contact*100) / len(pdays))
#print("Houve contatos para %i " %contacts + "clientes")
#print("NÃO houve contato para %i" %no_contact + " clientes na campanha anterior")
print("#============================================= Sub-CONCLUSÕES ===============================================")
print("")
print("#========================== quantidade de clientes contactados, aumentou ou diminuiu? =======================")
print("Houve contato de %i" %no_contact + " de clientes a mais do que na campanha anterior")
print("o que representa %.2f" %por_contacts + "% de clientes a mais contactados")       #respondido
print("#============================================================================================================")
print("")
#======================================================================= se houve contato anterior e quantos dias
# media e total de contatos campanha atual
total_call = sum(campaign)
mean_campaign = np.mean(campaign)
print("#======================= quantidade de ligações para clientes, aumentou ou diminuiu?  =======================")
print("O número total de ligações da campanha atual foi de %i"  %total_call)
print("O numero médio de ligações da campanha atual foi de %.2f" %mean_campaign)
# previous - campanha anterior
total_ligações = sum(previous)
media_ligações = np.mean(previous)
print("O número total de ligações da campanha anterior foi %i"  %total_ligações)
print("O numero médio de ligações da campanha anterior foi de %.2f" %media_ligações)
print("#------------------------------------------------------------------------------------------------------------")
dif_call = total_call - total_ligações          # campanha atual -  campanha anterior
dif_call_por = ((dif_call*100) / total_call)
print("Houve %i" %dif_call + " a mais de ligações na campanha atual com relação a campanha anterior, ou %.2f" %dif_call_por + "% a mais") #respondido
print("#============================================================================================================")
print("")

#======================================================================= sucesso da camapanha anterior
#CAMPANHA ATUAL
client_subscribed = future_client[future_client == 'yes']
quantidade_clientes = len(future_client)
per_success_atual = ((len(client_subscribed)*100) / quantidade_clientes)
print("#========= houve um aumento na taxa de sucesso, ou seja, taxa de clientes que assinaram a campanha?  =========")
print("O numero de clientes que assinaram é %i" %(len(client_subscribed)) + ", o que representa %.2f" %per_success_atual + "% sobre o total de " + str(quantidade_clientes) + " clientes")

#CAMPANHA ANTERIOR
# poutcome - resultado, baseando-se no se foi contactado ou nao (pdays) e na quantidade de ligações
#"unknown","other","failure","success"
total_poutcome = len(poutcome)
##print("Total de resultados %i" %total_poutcome)
#"unknown"
unknown = poutcome[poutcome == 'unknown']
len_unknown = len(unknown)
per_unknown = ((len_unknown*100) / (total_poutcome))
##print("Total de unknown %i" %len_unknown + " ou, %.2f" %per_unknown + "%")
#"other"
other = poutcome[poutcome == 'other']
len_other = len(other)
per_other = ((len_other*100) / (total_poutcome))
##print("Total de other %i" %len_other + " ou, %.2f" %per_other + "%")
###"failure"
failure = poutcome[poutcome == 'failure']
len_failure = len(failure)
per_failure = ((len_failure*100) / (total_poutcome))
##print("Total de failure %i"  %len_failure + " ou, %.2f" %per_failure + "%")
###"success"
success = poutcome[poutcome == 'success']
len_success = len(success)
per_success_ant = ((len_success*100) / (total_poutcome))
##print("Total de success %i" %len_success + " ou, %.2f" %per_success_ant + "%")
print("O numero de clientes que assinaram é %i" %len_success + ", o que representa %.2f" %per_success_ant + "% sobre o total de " + str(contacts) + " clientes")

# relação
if per_success_atual > per_success_ant:
    per_to = ((per_success_ant*100) / per_success_atual)
    aumentou_diminuiu = "aumento"
else:
    per_to = ((per_success_atual*100) / per_success_ant)
    aumentou_diminuiu = "diminuição"


per_to = ((per_success_ant*100) / per_success_atual)
print("Houve um " + aumentou_diminuiu + " de %.2f" %per_to + " da proporção de aceitação da campanha atual com relação a anterior")
print("")
print("#============================================= RESPOSTA ==================================================")
print("")
print("Os %.2f" %por_contacts + "% a mais de clientes junto do aumento de ligações de " + str(int(dif_call_por)) + "% a mais,")
print("contribuiram para o aumento de aceitação da campanha em %.2f" %per_to + "%")

