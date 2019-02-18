#!/bin/bash
# Activate virtual environment
. /appenv/bin/activate

# Install application test requirements
pip3 install -r requirements_test.txt

exec $@