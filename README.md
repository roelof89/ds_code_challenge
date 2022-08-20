
<img src="img/city_emblem.png" alt="City Logo"/>

# City of Cape Town - Data Science Unit Code Challenge
** please note I added this file to give feedback on which scripts to run, when and for what purpose
I renamed the original README.md as CREADME.md
Script files are labelled according to the task headers

# Purpose
Give feedback on the analysis and code I've produced for the challenge

# Setup
This project is built in python3.9 with a virtual environment.
```sh
# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# On windows
python3 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

# Project layout
This project has a few folders in which the work is structure.
* data: were the data will be housed(a script creates this dir and loads the files for use 0-fetch_data.py)
* run scripts are also in root
* notebooks are stored at root


# Fetch data
We won't load file into github. I built a script to pull the data from the url and populate the directories as needed.
```sh
python 0-fetch_data.py
```