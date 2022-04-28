# Developer: Aldrin Azucena - 001220471
# Assignment #3 - CPSC 4310
# Dataset from: https://www.kaggle.com/datasets/venky73/spam-mails-dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.naive_bayes import naive_bayes
from src.logic_regression import logic_regression
from src.model import define_data

# main function to run the program
def main():
    data = pd.read_csv('spam_ham_dataset.csv', index_col=0)
    features, labels = define_data(data)
    naive_bayes(features, labels)
    print('')
    logic_regression(features, labels)
    print('')

    
    
if __name__ == "__main__":
    main()
    


