In this challenge, the `list_files` function is vulnerable to OS command injection attacks because of the usage of `os.system(...)`. You are tasked with refactoring the code so that:
1. `list_files` is no longer vulnerable to OS command injection attacks.
2. `list_files` retains the original functionality to list all files in a given directory.

The test cases in `unsafe_functions_1` should pass.
