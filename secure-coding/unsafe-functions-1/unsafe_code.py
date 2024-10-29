### STARTING CODE ###
"""
Instructions:
1) Create a file named "unsafe_code.py" in /home/hacker.
2) Copy the below code and begin working there.
"""
#####################
import os

# Insecure Code: Uses os.system() to list files
def list_files(directory):
    os.system(f'ls {directory}')