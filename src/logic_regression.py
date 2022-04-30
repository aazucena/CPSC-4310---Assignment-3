from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
from src.model import get_reports
import matplotlib.pyplot as plt


def eval(features, labels):
    # Intialize the Logistic Regression Classifier
    model = LogisticRegression()

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        np.asarray(features), labels)

    # Train Logistic Regression Classifier based on the data
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate with the classification reports
    get_reports("Logic Regression", y_test, y_pred)
