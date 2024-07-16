# 1. Qual profissão tem mais tendência a fazer um empréstimo? De qual tipo?

import numpy as np
import pandas as pd

# import csv file
bank = pd.read_csv("bank-full.csv", sep=';')

# set and load variables job, housing and loan for future
job = np.array(bank['job'])
housing = np.array(bank['housing'])
loan = np.array(bank['loan'])

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

#====================================================================================================================================================== Personal Loan calc

# set workers with personan loan
job_loan = job[loan == 'yes']

# length of workes by type of job
admin_job_loan         = [len(job_loan[job_loan == 'admin.']),        'admin.']
unknown_job_loan       = [len(job_loan[job_loan == 'unknown']),       'unknown']
unemployed_job_loan    = [len(job_loan[job_loan == 'unemployed']),    'unemployed']
management_job_loan    = [len(job_loan[job_loan == 'management']),    'management']
housemaid_job_loan     = [len(job_loan[job_loan == 'housemaid']),     'housemaid']
entrepreneur_job_loan  = [len(job_loan[job_loan == 'entrepreneur']),  'entrepreneur']
student_job_loan       = [len(job_loan[job_loan == 'student']),       'student']
blue_collar_job_loan   = [len(job_loan[job_loan == 'blue-collar']),   'blue-collar']
self_employed_job_loan = [len(job_loan[job_loan == 'self-employed']), 'self-employed']
retired_job_loan       = [len(job_loan[job_loan == 'retired']),       'retired']
technician_job_loan    = [len(job_loan[job_loan == 'technician']),    'technician']
services_job_loan      = [len(job_loan[job_loan == 'services']),      'services']

# list
arr_job_loan = [ admin_job_loan, unknown_job_loan, unemployed_job_loan, management_job_loan, housemaid_job_loan,
                 entrepreneur_job_loan, student_job_loan, blue_collar_job_loan, self_employed_job_loan,
                 retired_job_loan, technician_job_loan, services_job_loan]

# job with more loan tendency
arr_job_loan_max = max(arr_job_loan)

# separation of value and name
arr_job_loan_max_value = arr_job_loan_max[0]
arr_job_loan_max_name  = arr_job_loan_max[1]

#====================================================================================================================================================== Final Result

# comparators for final result
if (arr_job_house_max_name == arr_job_loan_max_name) == True:       # compara, se os sub resultados indicarem a mesma profissão, já da logo o resultado final
    job_highest_loan_name = arr_job_house_max_name
    #type_of_loan = "Both"
else:                                                               # caso contrario, compara os valores e ve qual profissão pegou mais emprestimos
    if arr_job_loan_max_value > arr_job_house_max_value:
        job_highest_loan_name = arr_job_loan_max_name
        #type_of_loan = "Personal Loan"
    else:
        job_highest_loan_name = arr_job_house_max_name
        #type_of_loan = "House Loan"

if arr_job_loan_max_value > arr_job_house_max_value:
    job_highest_loan_name = arr_job_loan_max_name
    type_of_loan = "Loan"
else:
    job_highest_loan_name = arr_job_house_max_name
    type_of_loan = "Housing" 
        

# a profissão tem mais tendência a fazer um empréstimo
print("")
print("#============================================= RESPOSTA ==================================================")
print("")
print("A profissão que tem mais tendência a fazer um empréstimo é a: " + job_highest_loan_name)
print("Do tipo: " + type_of_loan)
