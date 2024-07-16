from sklearn.metrics import average_precision_score, mean_absolute_error, roc_curve, auc, roc_auc_score
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_curve
from scikitplot.metrics import plot_roc
from collections import Counter
import matplotlib.pyplot as plt

def conf_matrix(y_test, preds):
    # confusion matrix
    conf_matrix = confusion_matrix(y_test, preds)
    #print(conf_matrix)

    print('               Actual Values')
    print('           +--------+--------+')
    print('           | Neg(0) | Pos(1) |')
    print('p +--------+--------+--------+')
    print('r | Neg(0) | ' + str(conf_matrix[0][0]) + '  | ' + str(conf_matrix[0][1]) + '    |')
    print('e +--------+--------+--------+')
    print('d | Pos(1) | ' + str(conf_matrix[1][0]) + '   | ' + str(conf_matrix[1][1]) + '    |')
    print('s +--------+--------+--------+')
    
##############################################################################################################################
def aucur(y_test, preds):
    # calculate AUC
    aucur = roc_auc_score(y_test, preds)
    print('AUC: %.3f' % aucur)

    # calculate roc curve
    fpr, tpr, thresholds = roc_curve(y_test, preds)

    # plot no skill
    plt.plot([0, 1], [0, 1], linestyle='--')
    # plot the roc curve for the model
    plt.plot(fpr, tpr, marker='.')
    # show the plot
    plt.show()

##############################################################################################################################
def precision_recall_curve(y_test, preds):
    average_precision = average_precision_score(y_test, preds)

    precision, recall, _ = precision_recall_curve(y_test, preds)

    # In matplotlib < 1.5, plt.fill_between does not have a 'step' argument
    step_kwargs = ({'step': 'post'} if 'step' in signature(plt.fill_between).parameters
                                    else {})
    
    plt.step(recall, precision, color='b', alpha=0.2, where='post')
    plt.fill_between(recall, precision, alpha=0.2, color='b', **step_kwargs)

    plt.xlabel('Recall')
    plt.ylabel('Precision')

    plt.ylim([0.0, 0.02])
    plt.xlim([0.0, 1])

    plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(average_precision))
    
##############################################################################################################################
def roc_curves(X_test, y_test, pipeline):
    y_probas = pipeline.predict_proba(X_test)
    plot_roc(y_test, y_probas, plot_micro = False, plot_macro = False, figsize = (8, 8))
    plt.show()
