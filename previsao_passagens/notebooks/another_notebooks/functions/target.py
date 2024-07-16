from collections import Counter

def y_target(clients_sample, df_complainers):
    y = [0 for i in range(len(clients_sample))]

    for index, row in clients_sample.iterrows():
        # compara pra cada linha de df_complainers['cpf_cnpj_autor_encrypted'] com todas de clients_sample['cssocialsecno_encrypted']
        check = (df_complainers.cpf_cnpj_autor_encrypted == row.cssocialsecno_encrypted)

        if check.any(): 
            y[index] = 1

    print('Da base de ' + str(len(clients_sample)) + ' clientes, ' + str(y.count(1)) + 
    ' deles são reclamantes, ou seja, %.4f' %float((Counter(y)[1]/len(clients_sample))*100) + '%')
            
    return y