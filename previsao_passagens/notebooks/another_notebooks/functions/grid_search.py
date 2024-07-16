from sklearn.model_selection import ParameterGrid

def grid_search(X_train, X_test, y_train, y_test, model, pipeline):
    # Create a dictionary of hyperparameters to search
    #LogisticRegression
    grid = {
            'penalty'      : ['str', 'l1', 'l2', 'elasticnet', 'none']
            #'dual'         : [0.2, 0.4, 0.6], 
            #'criterion'    : ['gini', 'entropy'],
            #'C'            : [0.4, 0.8],
            #'solver'       : ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
            #'max_iter'     : [1, 2, 4],
            #'multi_class'  : ['ovr', 'multinomial', 'auto']
            }
    
    # DecisionTreeClassifier, RandomForestClassifier
#     grid = {
#             'n_estimators' : [50, 150, 250],
#             'max_depth'    : [14, 20, 24], 
#             'criterion'    : ['gini', 'entropy']
#             }

#     #XGB
#     grid = {
#             'n_estimators' : [50, 100, 150, 200, 250],
#             'max_depth'    : [14, 20, 24], 
#             'random_state' : [42]
#             'subsample'    : [0.8]
#             'max_depth'    : [20]
#             }

    test_scores = []

    # Loop through the parameter grid, set the hyperparameters, and save the scores
    for g in ParameterGrid(grid):
        model.set_params(**g, n_jobs=-1)  # ** is "unpacking" the dictionary
        pipeline.fit(X_train, y_train)
        test_scores.append(pipeline.score(X_test, y_test))

    # Find best hyperparameters from the test score and print
    best_idx = np.argmax(test_scores)
    print(test_scores[best_idx], ParameterGrid(grid)[best_idx])