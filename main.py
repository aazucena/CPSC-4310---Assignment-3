# Developer: Aldrin Azucena - 001220471
# Assignment #3 - CPSC 4310
# Dataset from: https://www.kaggle.com/datasets/venky73/spam-mails-dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src import naive_bayes, logic_regression, neural_network, model

# main function to run the program
def main():
    data = pd.read_csv('spam_ham_dataset.csv', index_col=0)
    features, labels = model.define_data(data)
    naive_bayes.eval(features, labels)
    print('')
    logic_regression.eval(features, labels)
    print('')
    neural_network.eval(features, labels)
    print('')

    
    
if __name__ == "__main__":
    main()
    


