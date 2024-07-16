import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
#import os
#print(os.listdir("../input"))

# database
data = pd.read_csv("database_versao_LatLongDecimal_fonteANM_23_01_2019.csv", sep=',')

print('')
missing_val_count_by_column = (data.isnull().sum())
print('Dados com NaN:')
print('')
print(missing_val_count_by_column[missing_val_count_by_column > 0])

# divide os dados para teste e treino
train = data[0:390]
test = data[390:714].reset_index()

# analise de dados parte 1

counter = 0
def check_data(tr_or_ts, col, counter):
    counter = 0
    for i in range(tr_or_ts[col].shape[0]):
        if (tr_or_ts[col][i] == '-') == True:
            counter += 1
    return counter

##MINERIO_PRINCIPAL
print('A feature MINERIO_PRINCIPAL no df train possui "', check_data(train, 'MINERIO_PRINCIPAL', counter), '" dados inválidos')
print('A feature MINERIO_PRINCIPAL no df test possui "', check_data(test, 'MINERIO_PRINCIPAL', counter), '" dados inválidos')
print('')
#---------------------------------------------------------------------------------------------------------------------------
#ALTURA_ATUAL_metros
print('A feature ALTURA_ATUAL_metros no df train possui "', check_data(train, 'ALTURA_ATUAL_metros', counter), '" dados inválidos')
print('A feature ALTURA_ATUAL_metros no df test possui "', check_data(test, 'ALTURA_ATUAL_metros', counter), '" dados inválidos')
print('')
#---------------------------------------------------------------------------------------------------------------------------
#VOLUME_ATUAL_m3
print('A feature VOLUME_ATUAL_m3 no df train possui "', check_data(train, 'VOLUME_ATUAL_m3', counter), '" dados inválidos')
print('A feature VOLUME_ATUAL_m3 no df test possui "', check_data(test, 'VOLUME_ATUAL_m3', counter), '" dados inválidos')
print('')
#---------------------------------------------------------------------------------------------------------------------------
#CATEGORIA_DE_RISCO
print('O target CATEGORIA_DE_RISCO no df train possui "', check_data(train, 'CATEGORIA_DE_RISCO', counter), '" dados inválidos')
print('')
#---------------------------------------------------------------------------------------------------------------------------
#DANO_POTENCIAL_ASSOCIADO
print('O target DANO_POTENCIAL_ASSOCIADO no df train possui "', check_data(train, 'DANO_POTENCIAL_ASSOCIADO', counter), '" dados inválidos')
print('')
#---------------------------------------------------------------------------------------------------------------------------
#CLASSE
print('O target CLASSE no df train possui "', check_data(train, 'CLASSE', counter), '" dados inválidos')
print('')


# Tratamento dos dados de treino

#train
# string to float64
train['ALTURA_ATUAL_metros'] = pd.concat([train['ALTURA_ATUAL_metros'].str.split().str[0].str.replace(',','').astype(float) for col in train], axis=1)
train['VOLUME_ATUAL_m3'] = pd.concat([train['VOLUME_ATUAL_m3'].str.split().str[0].str.replace(',','').astype(float) for col in train], axis=1)

#test
# Os dados de test estão com dados inválidos, precisam ser tratados para depois serem convertidos para float64.
test['ALTURA_ATUAL_metros'] = pd.concat([test['ALTURA_ATUAL_metros'].str.split().str[0].str.replace('-','') for col in test], axis=1) # converte - para nada
test['ALTURA_ATUAL_metros'] = pd.concat([test['ALTURA_ATUAL_metros'].str.split().str[0].str.replace('','') for col in test], axis=1)  # converte vazio para NaN
test['ALTURA_ATUAL_metros'] = pd.concat([test['ALTURA_ATUAL_metros'].str.split().str[0].str.replace(',','').astype(float) for col in test], axis=1) # float

test['VOLUME_ATUAL_m3'] = pd.concat([test['VOLUME_ATUAL_m3'].str.split().str[0].str.replace('-','') for col in test], axis=1) # converte - para nada
test['VOLUME_ATUAL_m3'] = pd.concat([test['VOLUME_ATUAL_m3'].str.split().str[0].str.replace('','') for col in test], axis=1) # converte vazio para NaN
test['VOLUME_ATUAL_m3'] = pd.concat([test['VOLUME_ATUAL_m3'].str.split().str[0].str.replace(',','').astype(float) for col in test], axis=1) #float

## make copy to avoid changing original data (when Imputing)
new_data = []
new_data = test[['ALTURA_ATUAL_metros', 'VOLUME_ATUAL_m3']]

## make new columns indicating what will be imputed
cols_with_missing = (col for col in new_data.columns 
                                 if new_data[col].isnull().any())
for col in cols_with_missing:
    new_data[col + '_was_missing'] = new_data[col].isnull()

## Imputation
my_imputer = SimpleImputer()
new_data = pd.DataFrame(my_imputer.fit_transform(new_data))
new_data.drop(columns=[2,3])

test['ALTURA_ATUAL_metros'] = new_data[0]
test['VOLUME_ATUAL_m3'] = new_data[1]

# Analise dos dados - parte 2

##MINERIO_PRINCIPAL
print('A feature MINERIO_PRINCIPAL no df train possui "', check_data(train, 'MINERIO_PRINCIPAL', counter), '" dados inválidos')
print('A feature MINERIO_PRINCIPAL no df test possui "', check_data(test, 'MINERIO_PRINCIPAL', counter), '" dados inválidos')
print('')
#---------------------------------------------------------------------------------------------------------------------------
#ALTURA_ATUAL_metros
print('A feature ALTURA_ATUAL_metros no df train possui "', check_data(train, 'ALTURA_ATUAL_metros', counter), '" dados inválidos')
print('A feature ALTURA_ATUAL_metros no df test possui "', check_data(test, 'ALTURA_ATUAL_metros', counter), '" dados inválidos')
print('')
#---------------------------------------------------------------------------------------------------------------------------
#VOLUME_ATUAL_m3
print('A feature VOLUME_ATUAL_m3 no df train possui "', check_data(train, 'VOLUME_ATUAL_m3', counter), '" dados inválidos')
print('A feature VOLUME_ATUAL_m3 no df test possui "', check_data(test, 'VOLUME_ATUAL_m3', counter), '" dados inválidos')
print('')
#---------------------------------------------------------------------------------------------------------------------------
#CATEGORIA_DE_RISCO
print('O target CATEGORIA_DE_RISCO no df train possui "', check_data(train, 'CATEGORIA_DE_RISCO', counter), '" dados inválidos')
print('')
#---------------------------------------------------------------------------------------------------------------------------
#DANO_POTENCIAL_ASSOCIADO
print('O target DANO_POTENCIAL_ASSOCIADO no df train possui "', check_data(train, 'DANO_POTENCIAL_ASSOCIADO', counter), '" dados inválidos')
print('')
#---------------------------------------------------------------------------------------------------------------------------
#CLASSE
print('O target CLASSE no df train possui "', check_data(train, 'CLASSE', counter), '" dados inválidos')
print('')

# One hot encoding

# one hot encoding
#MINERIO_PRINCIPAL
train_MINERIO_PRINCIPAL = pd.get_dummies(train['MINERIO_PRINCIPAL'])
test_MINERIO_PRINCIPAL  = pd.get_dummies(test['MINERIO_PRINCIPAL'])

#CATEGORIA_DE_RISCO
train_CATEGORIA_DE_RISCO = pd.get_dummies(train['CATEGORIA_DE_RISCO'])

#DANO_POTENCIAL_ASSOCIADO
train_DANO_POTENCIAL_ASSOCIADO = pd.get_dummies(train['DANO_POTENCIAL_ASSOCIADO'])

#CLASSE
train_CLASSE = pd.get_dummies(train['CLASSE'])


# Target and Features creation

#target
y = pd.concat([train_CATEGORIA_DE_RISCO, train_DANO_POTENCIAL_ASSOCIADO, train_CLASSE], axis=1, join_axes=[train_CATEGORIA_DE_RISCO.index])

#features
features = ['ALTURA_ATUAL_metros', 'VOLUME_ATUAL_m3']
#features_minerio = ['Aluvião Estanífero', 'Argila', 'Minério de Ouro Primário', 'Carvão Mineral Camada Bonito', 
#                    'Rocha Aurífera', 'Carvão Mineral', 'Minério de Vanádio', 'Bauxita Grau Não Metalúrgico', 
#                    'Minério de Nióbio', 'Areia', 'Sedimentos', 'Cascalho']

# I choosed this this features using permutation, I saw the features with more influence in training, after I edited with this features below
features_minerio = ['Aluvião Estanífero', 'Argila', 'Minério de Ouro Primário', 
                    'Rocha Aurífera', 'Bauxita Grau Não Metalúrgico', 'Cascalho']

X = pd.concat([train_MINERIO_PRINCIPAL[features_minerio], train[features]], axis=1, join_axes=[train_MINERIO_PRINCIPAL.index])


# 75% for train data and 25% for test data
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size=0.25,
                                                    random_state=1)


# Define the model

train_model = make_pipeline(Imputer(), RandomForestRegressor(random_state=1))
train_model.fit(X_train, y_train)


# Make predictions for "Train" data

from sklearn.metrics import mean_absolute_error
import eli5
from eli5.sklearn import PermutationImportance

# predict
train_predictions = train_model.predict(X_test)

#mae using cross validation
scores = cross_val_score(train_model, X, y, scoring='neg_mean_absolute_error')
print(scores)
print('Mean Absolute Error %2f' %(-1 * scores.mean()))

# permutation
perm = PermutationImportance(train_model, random_state=1).fit(X_test, y_test)
eli5.show_weights(perm, feature_names = X.columns.tolist())


# Make Predictions for "Test" data

# create test_X which comes from test_data but includes only the columns you used for prediction.
# The list of columns is stored in a variable called features
#features
X_test = pd.concat([test_MINERIO_PRINCIPAL[features_minerio], test[features]], axis=1, join_axes=[test_MINERIO_PRINCIPAL.index])
X_test = my_imputer.fit_transform(X_test)

# make predictions which we will submit. 
test_preds = train_model.predict(X_test)


# Invert one hot encoding
# invert one hot encoding
#CATEGORIA_DE_RISCO
list_CATEGORIA_DE_RISCO = []
for i in range(test_preds.shape[0]):
    if ((test_preds[i,0] >= test_preds[i,1]) & (test_preds[i,0] > test_preds[i,2])):
        res_CATEGORIA_DE_RISCO = 'Alta'
    elif ((test_preds[i,1] > test_preds[i,0]) & (test_preds[i,1] > test_preds[i,2])):
        res_CATEGORIA_DE_RISCO = 'Baixa'
    else:
        res_CATEGORIA_DE_RISCO = 'Média'
    list_CATEGORIA_DE_RISCO.append(res_CATEGORIA_DE_RISCO)
df_CATEGORIA_DE_RISCO = pd.DataFrame(list_CATEGORIA_DE_RISCO)

#CATEGORIA_DE_RISCO
list_DANO_POTENCIAL_ASSOCIADO = []
for i in range(test_preds.shape[0]):
    if ((test_preds[i,3] >= test_preds[i,4]) & (test_preds[i,3] > test_preds[i,5])):
        res_DANO_POTENCIAL_ASSOCIADO = 'Alta'
    elif ((test_preds[i,4] > test_preds[i,3]) & (test_preds[i,4] > test_preds[i,5])):
        res_DANO_POTENCIAL_ASSOCIADO = 'Baixa'
    else:
        res_DANO_POTENCIAL_ASSOCIADO = 'Média'
    list_DANO_POTENCIAL_ASSOCIADO.append(res_DANO_POTENCIAL_ASSOCIADO)
df_DANO_POTENCIAL_ASSOCIADO = pd.DataFrame(list_DANO_POTENCIAL_ASSOCIADO)

#CATEGORIA_DE_RISCO
list_CLASSE = []
for i in range(test_preds.shape[0]):
    if ((test_preds[i,6] >= test_preds[i,7]) & (test_preds[i,6] >= test_preds[i,8]) & (test_preds[i,6] >= test_preds[i,9]) & (test_preds[i,6] >= test_preds[i,10])):
        res_CLASSE = 'A'
    elif ((test_preds[i,7] >= test_preds[i,6]) & (test_preds[i,7] >= test_preds[i,8]) & (test_preds[i,7] >= test_preds[i,9]) & (test_preds[i,7] >= test_preds[i,10])):
        res_CLASSE = 'B'
    elif ((test_preds[i,8] >= test_preds[i,6]) & (test_preds[i,8] >= test_preds[i,7]) & (test_preds[i,8] >= test_preds[i,9]) & (test_preds[i,8] >= test_preds[i,10])):
        res_CLASSE = 'C'
    elif ((test_preds[i,9] >= test_preds[i,6]) & (test_preds[i,9] >= test_preds[i,7]) & (test_preds[i,9] >= test_preds[i,8]) & (test_preds[i,9] >= test_preds[i,10])):
        res_CLASSE = 'D'
    else:
        res_CLASSE = 'E'
    list_CLASSE.append(res_CLASSE)
df_CLASSE = pd.DataFrame(list_CLASSE)


# Merging Train data and Test data

test_drop = test.drop(['CATEGORIA_DE_RISCO', 'DANO_POTENCIAL_ASSOCIADO', 'CLASSE', 'INSERIDA_NA_PNSB', 'LATITUDE', 'LONGITUDE'], axis=1)

new_columns = pd.DataFrame({'CATEGORIA_DE_RISCO' : list_CATEGORIA_DE_RISCO,
                           'DANO_POTENCIAL_ASSOCIADO' : list_DANO_POTENCIAL_ASSOCIADO,
                           'CLASSE' : list_CLASSE,
                           'INSERIDA_NA_PNSB' : test.INSERIDA_NA_PNSB,
                           'LATITUDE' : test.LATITUDE,
                           'LONGITUDE' : test.LONGITUDE
                          })

test = pd.concat([test_drop, new_columns], axis=1)
test = test.drop(['index'], axis=1)

new_data = pd.concat([train, test])



# Output file


output = pd.DataFrame({'NOME_BARRAGEM_MINERACAO': new_data.NOME_BARRAGEM_MINERACAO,
                       'NOME_DO_EMPREENDEDOR' : new_data.NOME_DO_EMPREENDEDOR,
                       'CPF_CNPJ' : new_data.CPF_CNPJ,
                       'POSICIONAMENTO' : new_data.POSICIONAMENTO,
                       'UF' : new_data.UF,
                       'MUNICIPIO' : new_data.MUNICIPIO,
                       'MINERIO_PRINCIPAL' : new_data.MINERIO_PRINCIPAL,
                       'ALTURA_ATUAL_metros' : new_data.ALTURA_ATUAL_metros,
                       'VOLUME_ATUAL_m3' : new_data.VOLUME_ATUAL_m3,
                       'CATEGORIA_DE_RISCO' : new_data.CATEGORIA_DE_RISCO,
                       'DANO_POTENCIAL_ASSOCIADO' : new_data.DANO_POTENCIAL_ASSOCIADO,
                       'CLASSE' : new_data.CLASSE,
                       'INSERIDA_NA_PNSB' : new_data.INSERIDA_NA_PNSB,
                       'LATITUDE' : new_data.LATITUDE,
                       'LONGITUDE' : new_data.LONGITUDE
                          })
output.to_csv('submission.csv', index=False)


# graphs

biggest_dam = new_data['UF'].value_counts()[:5]
print(biggest_dam)


#import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

labels = ['MG', 'PA', 'SP', 'MT', 'BA']

biggest_states  = [biggest_dam[0], biggest_dam[1], biggest_dam[2], biggest_dam[3], biggest_dam[4]]

colors = ['green', 'yellow', 'red', 'blue', 'pink']

explode = [0.1, 0.1, 0.2, 0.1, 0.1]

# Create the figure with one row and two columns. Figsize will define the figure size
fig, axes = plt.subplots(figsize=(18,6))

# Create the pie chart on the first position with the given configurations
pie_1 = axes.pie(biggest_states, labels=labels, autopct='%1.1f%%', colors=colors, explode = explode, startangle=90)
axes.set_title('5 maiores estados em quantidade de barragens')
# Make both axes equal, so that the chart is round
axes.axis('equal')

# Adjust the space between the two charts
plt.subplots_adjust(wspace=1)
plt.show()


# quantidade de barragens com CATEGORIA_DE_RISCO alto, media e baixa

q_cat_risco = new_data['CATEGORIA_DE_RISCO'].value_counts()[:5]
cr_baixa = q_cat_risco[0]
cr_media = q_cat_risco[1]
cr_alta = q_cat_risco[2]
print(q_cat_risco)


q_dano = new_data['DANO_POTENCIAL_ASSOCIADO'].value_counts()[:5]
dano_baixa = q_dano[0]
dano_media = q_dano[1]
dano_alta = q_dano[2]
print(q_dano)


q_classe = new_data['CLASSE'].value_counts()[:5]
classe_c = q_classe[0]
classe_b = q_classe[1]
classe_e = q_classe[2]
classe_d = q_classe[3]
classe_a = q_classe[4]
print(q_classe)

# Situação das barragens com relação a CATEGORIA_DE_RISCO, DANO_POTENCIAL_ASSOCIADO e CLASSE no país:

#import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

labels = ['Baixa', 'Média', 'Alta']
labels_classe = ['A', 'B', 'C', 'D', 'E']

sizes_risco  = [q_cat_risco[0], q_cat_risco[1], q_cat_risco[2]]
sizes_dano   = [q_dano[0], q_dano[1], q_dano[2]]
sizes_classe = [classe_a, classe_b, classe_c, classe_d, classe_e]

colors = ['green', 'yellow', 'red']
colors_classe = ['red', 'purple', 'yellow', 'blue', 'green']

explode = [0.1, 0.1, 0.2]
explode_classe = [0.1, 0.1, 0.2, 0.1, 0.1]

# Create the figure with one row and two columns. Figsize will define the figure size
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(22,6))

# Create the pie chart on the first position with the given configurations
pie_1 = axes[0].pie(sizes_risco, labels=labels, autopct='%1.1f%%', colors=colors, explode = explode, startangle=90)
axes[0].set_title('CATEGORIA DE RISCO')
# Make both axes equal, so that the chart is round
axes[0].axis('equal')

# Same as above, for the second pie chart
pie_2 = axes[1].pie(sizes_dano, labels=labels, autopct='%1.1f%%', colors=colors, explode = explode, startangle=90)
axes[1].set_title('DANO POTENCIAL ASSOCIADO')
# Make both axes equal, so that the chart is round
plt.axis('equal')

# Same as above, for the second pie chart
pie_3 = axes[2].pie(sizes_classe, labels=labels_classe, autopct='%1.1f%%', colors=colors_classe, explode = explode_classe, startangle=90)
axes[2].set_title('CLASSE DA BARRAGEM')
# Make both axes equal, so that the chart is round
plt.axis('equal')

# Adjust the space between the two charts
plt.subplots_adjust(wspace=1)
plt.show()

# As 5 maiores medições de barragens em Minas Gerais com CATEGORIA_DE_RISCO alto, media e baixa, por cidade

#Quantidade de barragem em cada cidade de MG
mg_alto_risco = new_data.where((new_data['UF'] == "MG") & (new_data['CATEGORIA_DE_RISCO'] == "Alta"))['MUNICIPIO'].value_counts()[:5]
print('Alto Risco')
print(mg_alto_risco)
print('')
mg_medio_risco = new_data.where((new_data['UF'] == "MG") & (new_data['CATEGORIA_DE_RISCO'] == "Média"))['MUNICIPIO'].value_counts()[:5]
print('Médio Risco')
print(mg_medio_risco)
print('')
mg_baixo_risco = new_data.where((new_data['UF'] == "MG") & (new_data['CATEGORIA_DE_RISCO'] == "Baixa"))['MUNICIPIO'].value_counts()[:5]
print('Baixo Risco')
print(mg_baixo_risco)
print('')

#Quantidade de barragem em cada cidade de MG
mg_alto_dano = new_data.where((new_data['UF'] == "MG") & (new_data['DANO_POTENCIAL_ASSOCIADO'] == "Alta"))['MUNICIPIO'].value_counts()[:5]
print('Alto Dano')
print(mg_alto_dano)
print('')
mg_medio_dano = new_data.where((new_data['UF'] == "MG") & (new_data['DANO_POTENCIAL_ASSOCIADO'] == "Média"))['MUNICIPIO'].value_counts()[:5]
print('Médio Dano')
print(mg_medio_dano)
print('')
mg_baixo_dano = new_data.where((new_data['UF'] == "MG") & (new_data['DANO_POTENCIAL_ASSOCIADO'] == "Baixa"))['MUNICIPIO'].value_counts()[:5]
print('Baixo Dano')
print(mg_baixo_dano)
print('')

#Quantidade de barragem em cada cidade de MG
mg_classe_a = new_data.where((new_data['UF'] == "MG") & (new_data['CLASSE'] == "A"))['MUNICIPIO'].value_counts()[:5]
print('Classe A')
print(mg_classe_a)
print('')
mg_classe_b = new_data.where((new_data['UF'] == "MG") & (new_data['CLASSE'] == "B"))['MUNICIPIO'].value_counts()[:5]
print('Classe B')
print(mg_classe_b)
print('')
mg_classe_c = new_data.where((new_data['UF'] == "MG") & (new_data['CLASSE'] == "C"))['MUNICIPIO'].value_counts()[:5]
print('Classe C')
print(mg_classe_c)
print('')
mg_classe_d = new_data.where((new_data['UF'] == "MG") & (new_data['CLASSE'] == "D"))['MUNICIPIO'].value_counts()[:5]
print('Classe D')
print(mg_classe_d)
print('')
mg_classe_e = new_data.where((new_data['UF'] == "MG") & (new_data['CLASSE'] == "E"))['MUNICIPIO'].value_counts()[:5]
print('Classe E')
print(mg_classe_e)
print('')

# Situação das barragens em Minas Gerais com relação a CATEGORIA_DE_RISCO, DANO_POTENCIAL_ASSOCIADO e CLASSE

#plt.figure(1 , figsize = (15 , 7))
#new_data.where((new_data['UF'] == "MG")& (new_data['CATEGORIA_DE_RISCO'] == "Baixa"))['MUNICIPIO'].value_counts().plot(kind="bar")
#plt.xticks(rotation = 90)
#plt.title('Número de barragens por cidade em MG com categoria de risco Baixa')
#plt.show()
labels = ['Baixa', 'Média', 'Alta']
labels_classe = ['A', 'B', 'C', 'D', 'E']

mg_sizes_risco  = [mg_baixo_risco[0], mg_medio_risco[0], mg_alto_risco[0]]
mg_sizes_dano   = [mg_baixo_dano[0], mg_medio_dano[0], mg_alto_dano[0]]
mg_sizes_classe = [mg_classe_a[0], mg_classe_b[0], mg_classe_c[0], 0, mg_classe_e[0]]

mg_colors = ['green', 'yellow', 'red']
mg_colors_classe = ['red', 'purple', 'yellow', 'blue', 'green']

mg_explode = [0.1, 0.1, 0.2]
mg_explode_classe = [0.1, 0.1, 0.2, 0.1, 0.1]

# Create the figure with one row and two columns. Figsize will define the figure size
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(22,6))

# Create the pie chart on the first position with the given configurations
pie_1 = axes[0].pie(mg_sizes_risco, labels=labels, autopct='%1.1f%%', colors=mg_colors, explode = mg_explode, startangle=90)
axes[0].set_title('CATEGORIA DE RISCO')
# Make both axes equal, so that the chart is round
axes[0].axis('equal')

# Same as above, for the second pie chart
pie_2 = axes[1].pie(mg_sizes_dano, labels=labels, autopct='%1.1f%%', colors=mg_colors, explode = mg_explode, startangle=90)
axes[1].set_title('DANO POTENCIAL ASSOCIADO')
# Make both axes equal, so that the chart is round
plt.axis('equal')

# Same as above, for the second pie chart
pie_3 = axes[2].pie(mg_sizes_classe, labels=labels_classe, autopct='%1.1f%%', colors=mg_colors_classe, explode = mg_explode_classe, startangle=90)
axes[2].set_title('CLASSE DA BARRAGEM')
# Make both axes equal, so that the chart is round
plt.axis('equal')

# Adjust the space between the two charts
plt.subplots_adjust(wspace=1)
plt.show()

