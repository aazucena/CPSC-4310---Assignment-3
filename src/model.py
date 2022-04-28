from sklearn import preprocessing, metrics

def define_data(data):
    encoder = preprocessing.LabelEncoder()
    labels = encoder.fit_transform(data['label'].values)
    indices = encoder.fit_transform(data.index)
    values = encoder.fit_transform(data['text'].values)
    features = list(zip(indices, values))
    return features, labels

def get_results(type, y_test, y_pred):
    accuracy = round(metrics.accuracy_score(y_test, y_pred) * 100, 2)
    print("Accuracy for {}: {}%".format(type, accuracy))
    precision = round(metrics.precision_score(y_test, y_pred) * 100, 2)
    print("Precision for {}: {}%".format(type, precision))
    recall = round(metrics.recall_score(y_test, y_pred) * 100, 2)
    print("Recall for for {}: {}%".format(type, recall))
