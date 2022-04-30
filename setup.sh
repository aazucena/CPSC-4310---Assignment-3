echo "Unzipping the whole dataset from https://www2.aueb.gr/users/ion/data/enron-spam/"
sleep 2
tar -xvf archived.tar.gz

echo "Creating Python 3 Virtual Environment"
sleep 2
python -m venv venv

echo "You are all set to go, continue reading the instructions on README!"
sleep 2