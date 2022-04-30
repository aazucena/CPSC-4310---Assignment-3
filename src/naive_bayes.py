from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import numpy as np
from src.model import get_reports


def eval(features, labels):
    # Intialize the Naive Bayes Classifier
    model = GaussianNB()

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        np.asarray(features), labels)
    
    # Train Naive Bayes Classifier based on the data
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate with the classification reports
    get_reports("Gaussian Naive Bayes", y_test, y_pred)
