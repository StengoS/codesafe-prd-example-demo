Welcome to the refactoring module! This challenge will serve as a tutorial to how you will mainly be
completing the challenges in this specific module. "Start" this challenge, and then you can interact with it
by clicking on "Workspace" in the site's navigation bar or "VSCode Workspace" in the pop-up after the
challenge has successfully started. 

If you are unfamiliar with VSCode, here are the quick basics to get going:
- To open a terminal: Click on the three-lines icon at the top-left, hover over "Terminal", and click "New Terminal".
- To change it to dark-mode: Click on the gear icon at the bottom-left, hover over "Themes", click "Color Theme", and click on one of the themes listed under "dark themes".

Start by running the 'checker' Python executable by doing the following in the terminal: 
```
$ cd /challenge
$ ./checker
```
The executable will then give you further instructions.

NOTE: You are also able to run 'checker' by doing `$ python3 checker`. This is usually fine, but for this environment 
and platform, due to how permissions are handled so that you cannot simply read the flag, you MUST run 'checker' by
doing `$ ./checker` so that it can successfully read the flag and print it in the terminal. If you complete the tasks
for the challenges but use `$ python3 checker`, it will say all checks have passed but is unable to read the flag.
