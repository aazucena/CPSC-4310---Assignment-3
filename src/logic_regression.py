from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np
from src.model import get_results
import matplotlib.pyplot as plt


def logic_regression(features, labels):
    model = LogisticRegression()

    X_train, X_test, y_train, y_test = train_test_split(
        np.asarray(features), labels)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    
    confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
    
    print("Confusion Matrix on Logic Regression:", confusion_matrix)    

    get_results("Logic Regression", y_test, y_pred)
    
    # y_proba = model.predict_proba(X_test)[::,1]
    # false_positive_rate, true_positive_rate, _ = metrics.roc_curve(y_test, y_proba)
    # auc = metrics.roc_auc_score(y_test, y_proba)
    # plt.plot(false_positive_rate, true_positive_rate, label="text, index, auc="+str(auc))
    # plt.legend(loc=4)
    # plt.show()
