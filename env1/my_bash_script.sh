#!/bin/bash
echo "Hello from CLI"
echo "My env var is: ${PATH_TO_ENV}"
# Activate the virtual environment
pwd
#source ${PATH_TO_ENV}/.venv/bin/activate

python --version
# Run the Python script
python my_script.py
