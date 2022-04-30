echo "Unzipping the whole dataset from https://www2.aueb.gr/users/ion/data/enron-spam/"
ping 127.0.0.1 -n 3 > nul
powershell -command "Expand-Archive archived.zip ."

echo "Creating Python 3 Virtual Environment"
ping 127.0.0.1 -n 3 > nul
python -m venv venv

echo "You are all set to go, continue reading the instructions on README!"
ping 127.0.0.1 -n 3 > nul