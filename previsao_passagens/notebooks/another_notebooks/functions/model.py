from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.metrics import mean_absolute_error

# testes
# https://docs.google.com/document/d/1pjpX9xQPdVgeJjKakVSYuqRReEyrZesD3-aD61Z-0wQ/edit

def tunning(X_train, X_test, y_train, y_test, pipeline):
    def get_mae(max_leaf_nodes, X_train, X_test, y_train, y_test):
        #model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
        pipeline.fit(X_train, y_train)
        preds_val = pipeline.predict(X_test)
        mae = mean_absolute_error(y_test, preds_val)
        return mae
    
    for max_leaf_nodes in [5, 50, 500, 5000]:
        my_mae = get_mae(max_leaf_nodes, X_train, X_test, y_train, y_test)
        print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %4f" %(max_leaf_nodes, my_mae))

###################################################################################################################
def model_def():
    #LogisticRegression https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
    model = LogisticRegression()

###################################################################################################################
    #DecisionTreeClassifier https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
    #model = DecisionTreeClassifier(random_state=42)
    #model = DecisionTreeClassifier(random_state=1986, criterion='gini', max_depth=3)

###################################################################################################################
    #RandomForestClassifier https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
    #model = RandomForestClassifier(n_jobs=-1)
    #model = RandomForestClassifier(random_state=1986, criterion='gini', max_depth=10, n_estimators=50, n_jobs=-1)
    
###################################################################################################################
    #GradientBoostingClassifier https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html
    #model = GradientBoostingClassifier()

###################################################################################################################
    # #XGBClassifier https://xgboost.readthedocs.io/en/latest/python/python_api.html
    #model = XGBClassifier()
    #model = XGBClassifier(n_estimators=230, random_state=42, subsample=0.8, max_depth=20, verbosity=1, n_jobs=-1)
    
    return model