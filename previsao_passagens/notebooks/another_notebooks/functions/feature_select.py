from sklearn.feature_selection import RFE, RFECV
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression

# RFE
def recursive_feature_elimination(X_train, y_train, model):
    rfe = RFE(model, 2)
    rfe = rfe.fit(X_train, y_train)

    print(rfe.support_)
    print(rfe.ranking_)

    order = rfe.ranking_
    order

    feature_ranks = []
    for i in order:
        feature_ranks.append(f"{i}. {X_train.columns[i]}")
    print()
    print(feature_ranks)

###################################################################################################################
def recursive_feature_elimination_cv(X_train, y_train, model):
    rfe = RFECV(model, 2, cv=5)
    rfe = rfe.fit(X_train, y_train)

    print(rfe.support_)
    print(rfe.ranking_)

    order = rfe.ranking_
    order

    feature_ranks = []
    for i in order:
        feature_ranks.append(f"{i}. {X_train.columns[i]}")
    print()
    print(feature_ranks)
    
###################################################################################################################
# SelectFromModel
def select_from_model(X_train, y_train, model):
    #logreg = LogisticRegression(fit_intercept = False)
    model.fit(X_train, y_train)

    smf = SelectFromModel(model)
    smf.fit(X_train, y_train)

    feature_idx = smf.get_support()
    feature_name = X_train.columns[feature_idx]

    print(feature_idx)
    print()
    print(feature_name)