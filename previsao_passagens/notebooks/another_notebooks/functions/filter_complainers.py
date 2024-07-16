import pandas as pd 

def filter_complainers(jec_exemplaria, anatel_exemplaria, consumidor_gov_exemplaria, procon_exemplaria):
    #################################################################################################
    # Usuarios jec_exemplaria                        #Da base de 126303 clientes, 270 deles são reclamantes, ou seja, 0.2138%

    # set df
    df_jec_exemplaria = pd.read_csv(jec_exemplaria, sep=';', low_memory=False)

    # separate columns
    df_jec_exemplaria = df_jec_exemplaria[['cpf_cnpj_autor_encrypted']]

    df_jec_exemplaria   #Da base de 126303 clientes, 270 deles são reclamantes, ou seja, 0.2138%


    
    
    #################################################################################################
    # Usuarios anatel_exemplaria                      # Da base de 156292 clientes, 984 deles são reclamantes, ou seja, 0.6296%
    
    # set df
    df_anatel_exemplaria = pd.read_csv(anatel_exemplaria, low_memory=False)

    # separate columns
    df_anatel_exemplaria = df_anatel_exemplaria[['cpfusuario_encrypted', 
                                                 'cnpjusuario_encrypted']]

    # merge cpf and cnpj unsing ***replace***
    df_anatel_exemplaria['cpfusuario_encrypted'] = df_anatel_exemplaria['cpfusuario_encrypted'].\
                                                   replace(717768040883963444, 
                                                           df_anatel_exemplaria['cnpjusuario_encrypted'])

    # removing cnpjusuario_encrypted column
    df_anatel_exemplaria = df_anatel_exemplaria.drop(['cnpjusuario_encrypted'], axis=1)

    # rename columns
    df_anatel_exemplaria  = df_anatel_exemplaria.rename(columns={'cpfusuario_encrypted' : 'cpf_cnpj_autor_encrypted'})

    # head
    df_anatel_exemplaria    # Da base de 156292 clientes, 984 deles são reclamantes, ou seja, 0.6296%
    #df_anatel_exemplaria.iloc[10:16]

    
    
    
    #################################################################################################
    # usuarios consumidor_gov_exemplaria                       # Da base de 156292 clientes, 0 deles são reclamantes, ou seja, 0.0000%
        
    # set df
    df_consumidor_gov_exemplaria = pd.read_csv(consumidor_gov_exemplaria, sep=';', header=0)

    # separate columns
    df_consumidor_gov_exemplaria = df_consumidor_gov_exemplaria[['consumidor_encrypted']]

    # rename columns
    df_consumidor_gov_exemplaria = df_consumidor_gov_exemplaria.\
                                   rename(columns={'consumidor_encrypted' : 'cpf_cnpj_autor_encrypted'})

    # head
    df_consumidor_gov_exemplaria # Da base de 156292 clientes, 0 deles são reclamantes, ou seja, 0.0000%

    
    
    
    #################################################################################################
    # usuarios procon_exemplaria                             # Da base de 156292 clientes, 60 deles são reclamantes, ou seja, 0.0384%
    
    # set df
    df_procon_exemplaria = pd.read_csv(procon_exemplaria, sep=';', header=0)

    # separate columns
    df_procon_exemplaria = df_procon_exemplaria[['cpf_cnpj_autor_encrypted']]

    # rename columns
    df_procon_exemplaria = df_procon_exemplaria.rename(columns={'cpf_cnpj_autor_encrypted' : 'cpf_cnpj_autor_encrypted'})

    # head
    df_procon_exemplaria   # Da base de 156292 clientes, 60 deles são reclamantes, ou seja, 0.0384%

    
    
    
    #################################################################################################
    # reunião dos databases
    
    df_list = [df_jec_exemplaria, df_anatel_exemplaria, df_consumidor_gov_exemplaria, df_procon_exemplaria]
    df_complainers = pd.concat(df_list, ignore_index=True)

    # drop the duplicate rows
    df_complainers = df_complainers.drop_duplicates()
    df_complainers = df_complainers.reset_index()
    df_complainers = df_complainers.drop(['index'], axis=1)

    return df_complainers
