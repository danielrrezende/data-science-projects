# Get list of categorical variables
def var_cat(X):
    s = (X.dtypes == 'object')
    object_cols = list(s[s].index)
    print("Categorical variables: ", len(object_cols))
    print(object_cols)
    return object_cols


#########################################################################################################
# Criando uma lista de variaveis numéricas
def var_num(X):
    numerical_cols = [cname for cname in X.columns if X[cname].dtype in ['int64', 'float64']]
    print("Numerical variables: ", len(numerical_cols))
    print(numerical_cols)
    return numerical_cols


#########################################################################################################
# Descrição das variáveis categoricas com no máximo 3 colunas. Nestas serão feitos one hot encoder diretamente
def cat_less_three(object_cols, X):
    for objects in object_cols:
            if X[objects].describe()[1] <= 3:
                print('Name: ', objects)
                print('Possui ' + str(X[objects].describe()[1]) + ' categorias')
                print(X[objects].unique()) #criar lista de categorias
                print()
                
                
#########################################################################################################                
# Descrição das variáveis categoricas acima de 3 colunas. Nestas serão feitos uma reunião de categorias.
def cat_more_three(object_cols, X):
    for objects in object_cols:
            if X[objects].describe()[1] > 3:
                print('Name: ', objects)
                print('Possui ' + str(X[objects].describe()[1]) + ' categorias')
                print(X[objects].unique()) #criar lista de categorias
                print()