# 6 Quais são as características mais proeminentes de um cliente que possua empréstimo imobiliário?

import numpy as np
import pandas as pd

# import csv file
bank = pd.read_csv("bank-full.csv", sep=';')

# set and load variables
marital = np.array(bank['marital'])                 # estado civil
housing = np.array(bank['housing'])                 # quem tem financiamento de casa
balance = np.array(bank['balance'])                 # salarios
age = np.array(bank['age'])                         # idade
job = np.array(bank['job'])                         # trabalho

#======================================================================= estado civil
# estado civil, provavelmente são pessoas casadas
# enumerar pessoas que possuem financiamento por estado civil "married","divorced","single"

marital_housing_y = marital[housing == 'yes']                 # dentro de marital, olhar quem tem financiamento

married = marital_housing_y[marital_housing_y == 'married']   # dentro de marital_housing_y, olha quem é married
per_married = ((len(married)*100) / len(marital_housing_y))

divorced = marital_housing_y[marital_housing_y == 'divorced'] # dentro de marital_housing_y, olha quem é married
per_divorced = ((len(divorced)*100) / len(marital_housing_y))

single = marital_housing_y[marital_housing_y == 'single']     # dentro de marital_housing_y, olha quem é married
per_single = ((len(single)*100) / len(marital_housing_y))

if ((per_married > per_divorced) & (per_married > per_single)):
    quemmaisfinancia = "Casados aderem mais ao programa"
    top_finc = per_married
elif ((per_divorced > per_married) & (per_divorced > per_single)):
    quemmaisfinancia = "Divorciados aderem mais ao programa"
    top_finc = per_divorced
else:
    quemmaisfinancia = "Solteiros aderiram mais ao programa"
    top_finc = per_single

print('#============================================= RESPOSTA ==================================================')
print("#================ enumerar pessoas que possuem financiamento por estado civil ============================")
print("")
print("As pessoas com emprestimo e casadas são: %i" %len(married))
print("As pessoas com emprestimo e divorciadas são: %i" %len(divorced))
print("As pessoas com emprestimo e solteiras são: %i" %len(single))
print(quemmaisfinancia + " com %.2f" %top_finc + "%")
print("")
print("#=========================================================================================================")

#======================================================================= media idade
# idade media das pessoas que financiam
age_finc = age[housing == 'yes']
media_age_finc = np.mean(age_finc)
print("#================================================ idade media ============================================")
print("")
print("A idade media das pessoas que financiam: %i" %media_age_finc)
print("")
print("#=========================================================================================================")

#======================================================================= media salario
# media salario
balance_finc = balance[housing == 'yes']
media_balance_finc = np.mean(balance_finc)
print("#================================================ media salario ==========================================")
print("")
print("A media de salario das pessoas que financiam é de %i" %media_balance_finc + " euros")
print("")
print("#=========================================================================================================")

#======================================================================= job
# job
# "admin.","unknown","unemployed","management","housemaid","entrepreneur","student","blue-collar",
# "self-employed","retired","technician","services"

##job_finc = job[housing == 'yes']
##
##admin = 0
##unknown = 0
##unemployed = 0
##management = 0
##housemaid = 0
##entrepreneur = 0
##student = 0
##blue_collar = 0
##self_employed = 0
##retired = 0
##technician = 0
##services = 0
##
##for i in range(len(job_finc)):
##    if job_finc[i] == 'admin.':
##        admin += 1
##    elif job_finc[i] == 'unknown':
##        unknown += 1
##    elif job_finc[i] == 'unemployed':
##        unemployed += 1
##    elif job_finc[i] == 'management':
##        management += 1
##    elif job_finc[i] == 'housemaid':
##        housemaid += 1
##    elif job_finc[i] == 'entrepreneur':
##        entrepreneur += 1
##    elif job_finc[i] == 'student':
##        student += 1
##    elif job_finc[i] == 'blue_collar':
##        blue_collar += 1
##    elif job_finc[i] == 'self_employed':
##        self_employed += 1
##    elif job_finc[i] == 'retired':
##        retired += 1
##    elif job_finc[i] == 'technician':
##        technician += 1
##    else:
##        services += 1
#====================================================================================================================================================== Housing Loan calc

# set workers with housing loan seted 'yes' in housing
job_house = job[housing == 'yes']

# length of workes by type of job
admin_job_house         = [len(job_house[job_house == 'admin.']),        'admin.']
unknown_job_house       = [len(job_house[job_house == 'unknown']),       'unknown']
unemployed_job_house    = [len(job_house[job_house == 'unemployed']),    'unemployed']
management_job_house    = [len(job_house[job_house == 'management']),    'management']
housemaid_job_house     = [len(job_house[job_house == 'housemaid']),     'housemaid']
entrepreneur_job_house  = [len(job_house[job_house == 'entrepreneur']),  'entrepreneur']
student_job_house       = [len(job_house[job_house == 'student']),       'student']                                    
blue_collar_job_house   = [len(job_house[job_house == 'blue-collar']),   'blue-collar']
self_employed_job_house = [len(job_house[job_house == 'self-employed']), 'self-employed']
retired_job_house       = [len(job_house[job_house == 'retired']),       'retired']
technician_job_house    = [len(job_house[job_house == 'technician']),    'technician']
services_job_house      = [len(job_house[job_house == 'services']),      'services']

# list
arr_job_house = [admin_job_house, unknown_job_house, unemployed_job_house, management_job_house,   
		housemaid_job_house, entrepreneur_job_house, student_job_house, blue_collar_job_house,  
		self_employed_job_house, retired_job_house, technician_job_house, services_job_house]

# job with more loan tendency
arr_job_house_max = max(arr_job_house)

# separation of value and name
arr_job_house_max_value = arr_job_house_max[0]
arr_job_house_max_name  = arr_job_house_max[1]

print("#================================================ media salario ==========================================")
print("")
print("A profissão que tem mais tendência a fazer um empréstimo é a: " + arr_job_house_max_name)
print(str(arr_job_house_max_value) + " pessoas com esta profissão fizeram emprestimo")
print("")
print("#=========================================================================================================")
