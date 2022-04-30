# Developer: Aldrin Azucena - 001220471
# Assignment #3 - CPSC 4310
# All Dataset are from: https://www2.aueb.gr/users/ion/data/enron-spam/

from os import listdir
from os.path import isfile, isdir, join
import csv
import codecs
import pandas as pd
import numpy as np
from timeit import default_timer as timer
from src import naive_bayes, logic_regression, neural_network, model

# read all files from spam & ham by specific folder
def getData(folder):
        preproDir = './preprocessed/'
        
        start = timer()
        # retrieve file names within ham and spam dir
        hamFiles = np.array([{ '': listdir(preproDir + folder + '/ham/').index(f),'label': 'ham', 'text': '', 'label_num': 0, 'folder': folder, 'path': preproDir + folder + '/ham/' + f, } for f in listdir(preproDir + folder + '/ham/') if isfile(join(preproDir + folder + '/ham/', f))])
        spamFiles = np.array([{ '': listdir(preproDir + folder + '/spam/').index(f),'label': 'spam', 'text': '', 'label_num': 1, 'folder': folder, 'path': preproDir + folder + '/spam/' + f, } for f in listdir(preproDir + folder + '/spam/') if isfile(join(preproDir + folder + '/spam/', f))])        
        print("Elapsed time for search and format files:", timer() - start, 'seconds')
        cstart = timer()
        files = np.concatenate((hamFiles, spamFiles), axis=None)
        print(len(files))
        print("Elapsed time to combine two large arrays files:", timer() - cstart, 'seconds')
        
        return files

# read all files from spam & ham
def getAllData():
        preproDir = './preprocessed/'
        
        start = timer()
        folders = np.array([f for f in listdir(preproDir) if isdir(join(preproDir, f))])
        print(folders)
        print("Elapsed time for search folders:", timer() - start, 'seconds')
        
        start = timer()
        # retrieve file names within ham and spam dir
        hamFiles = np.array([{ '': listdir(preproDir + folder + '/ham/').index(f),'label': 'ham', 'text': '', 'label_num': 0, 'folder': folder, 'path': preproDir + folder + '/ham/' + f, } for folder in folders for f in listdir(preproDir + folder + '/ham/') if isfile(join(preproDir + folder + '/ham/', f))])
        spamFiles = np.array([{ '': listdir(preproDir + folder + '/spam/').index(f),'label': 'spam', 'text': '', 'label_num': 1, 'folder': folder, 'path': preproDir + folder + '/spam/' + f, } for folder in folders for f in listdir(preproDir + folder + '/spam/') if isfile(join(preproDir + folder + '/spam/', f))])        
        print("Elapsed time for search and format files:", timer() - start, 'seconds')
        
        cstart = timer()
        files = np.concatenate((hamFiles, spamFiles), axis=None)
        print(len(files))
        print("Elapsed time to combine two large arrays files:", timer() - cstart, 'seconds')
        
        return files

get = {
    'enron1': getData,
    'enron2': getData,
    'enron3': getData,
    'enron4': getData,
    'enron5': getData,
    'enron6': getData,
    'All': getAllData,
    'all': getAllData,
    '': getAllData,
}
    
def init(folder=''):
    try: 
        # get files
        files = get[folder](folder) if folder not in ['All', 'all', ''] else get[folder]()
        
        # # get the file contents to array
        dstart = timer()
        for file in files:
            with codecs.open(file['path'], 'r', encoding="utf8", errors='ignore') as f:
                nstart = timer()
                file['text'] = '{}'.format(''.join(f.readlines()))
                print("Elapsed time get content from file `{}`: {}".format(file['path'], timer() - nstart))
        print("Elapsed time to get file contents:", timer() - dstart, 'seconds')
        

        # # convert and migrate to csv file
        estart = timer()
        with open('dataset_spam_ham.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['', 'label', 'text', 'label_num', 'folder', 'path'])
            writer.writeheader()
            for file in files:
                writer.writerow(file)
            csvfile.close()
        print("Elapsed time to convert the array of dict data to the .csv file:", timer() - estart, 'seconds')
        
        print('imported, converted, & migrated existing dataset into dataset_spam_ham.csv')
        
    except:
        print('failed to import dataset')



# main function to run the program
def main():
    print('Choose one of these folders or all of them to continue the program: ')
    print('\t- enron1')
    print('\t- enron2')
    print('\t- enron3')
    print('\t- enron4')
    print('\t- enron5')
    print('\t- enron6')
    print('\t- All (or none): WARNING it takes 2 - 3 minutes!!')
    inp = input('You typed: ')
    init(inp)
    
    data = pd.read_csv('dataset_spam_ham.csv', index_col=0)
    print(data)
    features, labels = model.define_data(data)
    naive_bayes.eval(features, labels)
    print('')
    logic_regression.eval(features, labels)
    print('')
    neural_network.eval(features, labels)
    print('')

    
    
if __name__ == "__main__":
    main()
    


