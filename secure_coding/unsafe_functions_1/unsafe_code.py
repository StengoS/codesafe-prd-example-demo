### STARTING CODE ###
"""
Note that the infrastructure will NOT let you modify any code in /challenge.

Instructions:
1) Create a file named "unsafe_code.py" in /home/hacker.
2) Copy the below code and begin working there.
"""
#####################
import os

# Given a string directory value, list all the files using 'ls' with os.system(...).
def list_files(directory):
    os.system(f'ls {directory}')