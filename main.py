# Developer: Aldrin Azucena - 001220471
# Assignment #3 - CPSC 4310
# Dataset from: http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron1.tar.gz


from os import listdir
from os.path import isfile, join
import csv

# read all files from spam & ham
def init(dataSize = 20):
    try: 
        hamDir = './enron1/ham/'
        spamDir = './enron1/spam/'
        
        # retrieve file names within ham and spam dir
        hamFiles = [f for f in listdir(hamDir) if isfile(join(hamDir, f))]
        spamFiles = [f for f in listdir(spamDir) if isfile(join(spamDir, f))]
        
        hamContent = []
        spamContent = []
        
        # get the file contents to array
        for hf in hamFiles[0:dataSize]:
            with open(hamDir + hf, 'r') as hfile:
                hamContent.append('{}'.format(''.join(hfile.readlines())))
                
        for sf in spamFiles[0:dataSize]:
            with open(spamDir + sf, 'r') as sfile:
                spamContent.append('{}'.format(''.join(sfile.readlines())))

        # convert and migrate to csv file
        with open('ham.csv', 'w', newline='') as hcsvfile:
            hwriter = csv.writer(hcsvfile)
            hwriter.writerow(('filename', 'content'))
            for hc in hamContent:
                hwriter.writerow((hamFiles[hamContent.index(hc)], hc))
            hcsvfile.close()
        with open('spam.csv', 'w', newline='') as scsvfile:
            swriter = csv.writer(scsvfile)
            swriter.writerow(('filename', 'content'))
            for sc in spamContent:
                swriter.writerow((spamFiles[spamContent.index(sc)], sc))
            scsvfile.close()
            
        print('imported, converted, & migrated existing dataset into ham.csv and spam.csv')
        
    except:
        print('failed to import dataset')

# main function to run the program
def main():
    init()
    
if __name__ == "__main__":
    main()
    


