# Developer: Aldrin Azucena - 001220471
# Assignment #3 - CPSC 4310
# Dataset from: https://www.kaggle.com/datasets/venky73/spam-mails-dataset


from os import listdir
from os.path import isfile, join
import pandas
import numpy as np

# main function to run the program
def main():
    data = pandas.read_csv('spam_ham_dataset.csv', index_col=0)
    print(data)
    
    
if __name__ == "__main__":
    main()
    


