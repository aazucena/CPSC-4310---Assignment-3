from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np
from src.model import get_results

def naive_bayes(features, labels):
    model = GaussianNB()

    X_train, X_test, y_train, y_test = train_test_split(
        np.asarray(features), labels)
    
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    get_results("Gaussian Naive Bayes", y_test, y_pred)
