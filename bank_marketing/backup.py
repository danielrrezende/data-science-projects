# backup

admin_job_len         = len(job_house[job_house == 'admin.'])
unknown_job_len       = len(job_house[job_house == 'unknown'])
unemployed_job_len    = len(job_house[job_house == 'unemployed'])
management_job_len    = len(job_house[job_house == 'management'])
housemaid_job_len     = len(job_house[job_house == 'housemaid'])
entrepreneur_job_len  = len(job_house[job_house == 'entrepreneur'])
student_job_len       = len(job_house[job_house == 'student'])                                    
blue_collar_job_len   = len(job_house[job_house == 'blue-collar'])
self_employed_job_len = len(job_house[job_house == 'self-employed'])
retired_job_len       = len(job_house[job_house == 'retired'])
technician_job_len    = len(job_house[job_house == 'technician'])
services_job_len      = len(job_house[job_house == 'services'])


arr_job_house = [ admin_job_len, unknown_job_len, unemployed_job_len, management_job_len, housemaid_job_len,
                  entrepreneur_job_len, student_job_len, blue_collar_job_len, self_employed_job_len,
                  retired_job_len, technician_job_len, services_job_len]



admin_job_loan         = len(job_loan[job_loan == 'admin.'])
unknown_job_loan       = len(job_loan[job_loan == 'unknown'])
unemployed_job_loan    = len(job_loan[job_loan == 'unemployed'])
management_job_loan    = len(job_loan[job_loan == 'management'])
housemaid_job_loan     = len(job_loan[job_loan == 'housemaid'])
entrepreneur_job_loan  = len(job_loan[job_loan == 'entrepreneur'])
student_job_loan       = len(job_loan[job_loan == 'student'])                                    
blue_collar_job_loan   = len(job_loan[job_loan == 'blue-collar'])
self_employed_job_loan = len(job_loan[job_loan == 'self-employed'])
retired_job_loan       = len(job_loan[job_loan == 'retired'])
technician_job_loan    = len(job_loan[job_loan == 'technician'])
services_job_loan      = len(job_loan[job_loan == 'services'])

arr_job_loan = [ admin_job_loan, unknown_job_loan, unemployed_job_loan, management_job_loan, housemaid_job_loan,
                 entrepreneur_job_loan, student_job_loan, blue_collar_job_loan, self_employed_job_loan,
                 retired_job_loan, technician_job_loan, services_job_loan]