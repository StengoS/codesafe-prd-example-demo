In this challenge, the `list_files` function is vulnerable to OS command injection attacks because of the usage of `os.system(...)`. You are tasked with refactoring the code in `unsafe_code.py` so that:
1. `list_files` is no longer vulnerable to OS command injection attacks.
2. `list_files` raises a `ValueError` when there is any error (including invalid syntax)
3. `list_files` is changed to return a list of file names of a given directory.

You do not need to add or adjust any of the test cases in `checker`. You may write helper functions in `unsafe_code.py`, 
but since you cannot adjust the test cases, do NOT adjust the original `list_files` function header. You must modify 
`unsafe_code.py` in the `/challenge` directory, but there is a non-writable copy in `/challenge/backup` in case you need
to restore the original and start over.

The `/challenge/some` directory is there for the test cases, but you are unable to modify anything there.

All of the test cases in `checker` must pass for the Python executable to give you the flag. In this challenge, 
you can read (but not write!) the checker script. 

Make sure to run the `checker` script by doing the following in the `/challenge` directory:
```
$ ./checker
```
