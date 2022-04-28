# Developer: Aldrin Azucena - 001220471
# Assignment #3 - CPSC 4310
# Dataset from: https://www.kaggle.com/datasets/venky73/spam-mails-dataset


from os import listdir
from os.path import isfile, join
import pandas

# main function to run the program
def main():
    data = pandas.read_csv('spam_ham_dataset.csv')
    columns = data.columns
    data.head()
    
    
if __name__ == "__main__":
    main()
    


