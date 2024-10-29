import os

# Insecure Code: Uses os.system() to list files
def list_files(directory):
    os.system(f'ls {directory}')