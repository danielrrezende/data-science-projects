from sklearn.model_selection import ParameterGrid

def grid_search(X_train, X_test, y_train, y_test, model):
    # Create a dictionary of hyperparameters to search
    #RandomForestClassifier 14:11 14:19
    grid = {
            'n_estimators' : [50, 100, 150],
            'max_depth'    : [2,3,4], 
            'min_samples_leaf' : [0.1, 0.3, 1]
            }
    
    # # standard -> GradientBoostingClassifier(criterion='friedman_mse', init=None,
    #                            learning_rate=0.1, loss='deviance', max_depth=3,
    #                            max_features=None, max_leaf_nodes=None,
    #                            min_impurity_decrease=0.0, min_impurity_split=None,
    #                            min_samples_leaf=1, min_samples_split=2,
    #                            min_weight_fraction_leaf=0.0, n_estimators=100,
    #                            n_iter_no_change=None, presort='auto',
    #                            random_state=None, subsample=1.0, tol=0.0001,
    #                            validation_fraction=0.1, verbose=0,
    #                            warm_start=False)
    
#     GradientBoostingClassifier # 13:43 14:51
#     grid = {'n_estimators'     : [50, 100, 150],
#             'max_depth'        : [2,3,4], 
#             'max_features'     : [0.25, 0.50, 0.75],
#             'min_samples_leaf' : [0.1, 0.3, 1],
#             'subsample'        : [0.3, 0.6, 1],
#             'random_state'     : [42]}

    #XGB
    # grid = {'objective'    : ['binary:logistic'], 
    #         'max_depth'    : [2,3,4], 
    #         'max_features' : [0.25, 0.50, 0.75],
    #         'learning_rate': [0.1, 0.01],
    #         'subsample'    : [0.3, 0.6],
    #         'random_state' : [42]}


    test_scores = []

    # Loop through the parameter grid, set the hyperparameters, and save the scores
    for g in ParameterGrid(grid):
        model.set_params(**g)  # ** is "unpacking" the dictionary
        model.fit(X_train, y_train)
        test_scores.append(model.score(X_test, y_test))

    # Find best hyperparameters from the test score and print
    best_idx = np.argmax(test_scores)
    print(test_scores[best_idx], ParameterGrid(grid)[best_idx])