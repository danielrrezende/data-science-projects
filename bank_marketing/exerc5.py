# 5. Qual o fator determinante para que o banco exija um seguro de crédito?

import numpy as np
import pandas as pd

# import csv file
bank = pd.read_csv("bank-full.csv", sep=';')

# set and load variables job, housing and loan for future
job = np.array(bank['job'])
housing = np.array(bank['housing'])
loan = np.array(bank['loan'])
credit = np.array(bank['default'])

# tem credito e tem emprego?
#"yes","no"
len_job = len(job)

job_credit_y = job[credit == 'yes']        # empregos e credito
job_credit_n = job[credit == 'no']         # empregos e nao tem credito

unemployed_credit_y = 0                     # não tem emprego e tem credito
employed_credit_y = 0                       # tem emprego e tem credito

unemployed_credit_n = 0                     # não tem emprego e não tem credito
employed_credit_n = 0                       # tem emprego e não tem credito
 
for i in range(len(job_credit_y)):  
	if job_credit_y[i] == 'unemployed':
		unemployed_credit_y += 1
	else:
		employed_credit_y += 1

for i in range(len(job_credit_n)):  
	if job_credit_n[i] == 'unemployed':
		unemployed_credit_n += 1
	else:
		employed_credit_n += 1
		
per_employed_credit_y = ((employed_credit_y*100) / len(job_credit_y))

print("#============================================= Sub-CONCLUSÕES ===============================================")
print("")
print("#========================================= tem credito e tem emprego?  ======================================")
print("A quantidade de pessoas que possuem emprego e possuem credito é %i" %employed_credit_y)
print("A quantidade de pessoas que possuem emprego e NÃO possuem credito é %i" %employed_credit_n)
print("A quantidade de pessoas que NÃO possuem emprego e possuem credito é %i" %unemployed_credit_y)
print("A quantidade de pessoas que NÃO possuem emprego e NÃO possuem credito é %i" %unemployed_credit_n)
print("#============================================================================================================")
print("")


# tem credito e já tem financiamento de casa
#"yes","no"
# quem tem credito, tem financiamento de casa?
credit_y_housing_y = credit[housing == 'yes']       # dentro de credit(col default), quem tem financiamento de casa
credit_y_housing_n = credit[housing == 'no']        # dentro de credit(col default), quem não tem financiamento de casa
# quem tem financiamento de casa, tem credito?
credit_n_housing_y = housing[credit == 'yes']      # dentro de housing, quem tem credito
credit_n_housing_n = housing[credit == 'no']       # dentro de housing, quem não tem credito


# quem tem credito, tem financiamento pessoal?
credit_y_loan_y = credit[loan == 'yes']       # dentro de credit(col default), quem tem financiamento pessoal (loan)
credit_y_loan_n = credit[loan == 'no']        # dentro de credit(col default), quem não tem financiamento pessoal (loan)
# quem tem financiamento pessoal, tem credito?
credit_n_loan_y = loan[credit == 'yes']       # dentro de loan, quem tem credito
credit_n_loan_n = loan[credit == 'no']        # dentro de loan, quem não tem credito


print("#========================================= tem credito finaciamento de casa =================================")
print("A quantidade de pessoas que tem credito e financiamento de casa é %i" %len(credit_y_housing_y))
print("A quantidade de pessoas que tem credito e NÃO financiamento de casa é %i" %len(credit_y_housing_n))
print("A quantidade de pessoas que NÃO possuem credito e possuem financiamento de casa é %i" %len(credit_n_housing_y))
print("A quantidade de pessoas que NÃO possuem credito e NÃO possuem financiamento de casa é %i" %len(credit_n_housing_n))
print("#============================================================================================================")
print("")

print("#========================================= tem credito finaciamento de pessoal ==============================")
print("A quantidade de pessoas que tem credito e financiamento pessoal é %i" %len(credit_y_loan_y))
print("A quantidade de pessoas que tem credito e NÃO financiamento pessoal é %i" %len(credit_y_loan_n))
print("A quantidade de pessoas que NÃO possuem credito e possuem financiamento pessoal é %i" %len(credit_n_loan_y))
print("A quantidade de pessoas que NÃO possuem credito e NÃO possuem financiamento pessoal é %i" %len(credit_n_loan_n))
print("#============================================================================================================")
print("")

total_credit = credit[credit == 'no']
total_housing = housing[housing == 'no']
total_loan   = loan[loan == 'no']
total_loans = len(total_housing) + len(total_loan)

print("#============================================= RESPOSTA ===================================================")
print("O fator determinante para que o banco exija um seguro de crédito é pelo fato de haver um elevado numero")
print("de pessoas que não possuem credito (%i" %len(total_credit) + ") nem financiamento (%i" %total_loans + ")")
print("O que aumenta a desconfiança dos bancos ao gerar emprestimos")

