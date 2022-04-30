Write-Output "Unzipping the whole dataset from https://www2.aueb.gr/users/ion/data/enron-spam/"
Start-Sleep -Seconds 2
Expand-Archive archived.zip -DestinationPath . -Force -Verbose

Write-Output "Creating Python 3 Virtual Environment"
Start-Sleep -Seconds 2
python -m venv venv

Write-Output "You are all set to go, continue reading the instructions on README!"
Start-Sleep -Seconds 2