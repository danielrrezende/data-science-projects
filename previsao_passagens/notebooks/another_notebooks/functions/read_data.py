import pandas as pd

def benchmark_reader(list_clients):
    client_chunks = []
    for file in list_clients:

            df_clients = pd.read_csv(file, sep = ";", 
                                     header = 0, 
                                     index_col = False, 
                                     names = None, 
                                     low_memory = False, 
                                     chunksize = 10**5) 

            for chunk in df_clients:

                new_clients = pd.DataFrame(chunk)

                # filter data chunk with frac percentage
                new_clients = new_clients.sample(frac = 0.045) #Da base de 126303 clientes, 1371 deles são reclamantes, ou seja, 1.0855%
                new_clients = new_clients.drop_duplicates(subset='cssocialsecno_encrypted', keep='first')
                
                # saves to list
                client_chunks.append(new_clients)

    clients = pd.concat(client_chunks).reset_index(drop = True)

    return clients