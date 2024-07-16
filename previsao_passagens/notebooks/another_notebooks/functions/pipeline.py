from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from mlxtend.feature_selection import ColumnSelector
from sklearn.pipeline import FeatureUnion
from functions.model import model_def

def f_pipeline(numerical_cols, object_cols):
    # Pré-processamento para Dados Numéricos # https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html
    numerical_transformer = Pipeline([
                                      ('imputer', SimpleImputer(strategy = 'constant')),
                                      ('scaler', StandardScaler())                       # muda valores de escala para valores menores
                                    ])

    ###################################################################################################################
    # Pré-processamento para Dados Categóricos
    categorical_transformer = Pipeline([
                                        ('imputer', SimpleImputer(strategy='most_frequent')),
                                        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False))
                                       ])
    
    ###################################################################################################################
    # Pré-processamento de pacote de dados numéricos e categóricos
    preprocessor = ColumnTransformer(transformers=[
                                                   ('num', numerical_transformer, numerical_cols),
                                                   ('cat', categorical_transformer, object_cols)
                                                  ], n_jobs=-1)
    
    ###################################################################################################################
    # MODEL
    model = model_def()

    ###################################################################################################################
    ## Bundle preprocessing and modeling code in a pipeline
    threshold_n=0.95
    
    pipeline = Pipeline(steps=[
                               ('preprocessor', preprocessor),
                               ('smote', SMOTE(random_state=42, n_jobs=-1)),   # equilibrar
                               ('pca', PCA(n_components = 1)),                 # reduzir numero de features sem fica com 0.511
                               ('model', model)
                              ])
    
    return pipeline, model
