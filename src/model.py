from sklearn import preprocessing, metrics

# organize and format the dataset
def define_data(data):
    encoder = preprocessing.LabelEncoder()
    labels = encoder.fit_transform(data['label'].values)
    indices = encoder.fit_transform(data.index)
    values = encoder.fit_transform(data['text'].values)
    features = list(zip(indices, values))
    return features, labels

# evaluate the score
def get_reports(type, y_test, y_pred):
    print('Reports for {}'.format(type))
    print('')
    print('Confusion Matrix:')
    print(metrics.confusion_matrix(y_test, y_pred))
    print('')
    print('Classification Report:')
    print(metrics.classification_report(y_test, y_pred))
    

