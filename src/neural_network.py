from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from src.model import get_reports


def eval(features, labels):
    model = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)

    X_train, X_test, y_train, y_test = train_test_split(
        np.asarray(features), labels)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    get_reports("MLP Neural Network", y_test, y_pred)
