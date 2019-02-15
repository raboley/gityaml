#!/bin/bash

# Create and initialize a Python Virtual Environment
write-host "Creating virtual env - env"
python -m virtualenv env

write-host "sourcing virtual env - env"
. env\Scripts\activate

# Install requirements 
write-host "pip installing requirements from requirements file in target directory"
pip install -r requirements.txt 
write-host "pip installing requirements from test requirements file in target directory"
pip install -r requirements-test.txt 