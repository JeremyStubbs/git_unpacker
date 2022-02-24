# Must "git add ." and "git commit -m "message"" first
# cd into repo first
# only works on linux
# specify export path

import os 
import re
from pathlib import Path
import shutil
import asyncio

# destination = os.environ("read")

# Initialize functions to perform "pwd", "ls", "ls -a", "git branch -a"

def get_path(): 
    return os.popen("pwd").read()[:-1]

def ls():
    return os.popen("ls").read()[:-1]

def lsa():
    return os.popen("ls -a").read()[:-1]


def branches():
    branches =  os.popen("git branch -a").read()[:-1].split("\n")
    pattern = re.compile(r'^(?!remotes).+')
    matches = []
    for branch in branches:
        x = branch.lstrip()
        if x[0]=="*":
                x=x[1:].lstrip()
        if pattern.match(x):
            matches.append(x)
    return matches

# Function to copy contents of each branch to a folder called "copy" on desktop
async def copy(name):
    os.popen("git checkout "+name)
    print(">>>Waiting to switch branches")
    await asyncio.sleep(2)
    os.popen(f"cp -R {directory} /Users/jeremystubbs/Desktop/copy/{name}" )
    print('>>>Copied folder')

# Eventually will worked for nested folders. For now can go to path manually.
directory = "/Users/jeremystubbs/Desktop/test"
os.chdir(directory)


# Make folder called "copy" in desktop - delete if already exists
dirpath = Path("/Users/jeremystubbs/Desktop/copy")
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)

os.mkdir("/Users/jeremystubbs/Desktop/copy")

# Get branches
the_branches = branches()
print(the_branches)

# Call copy on each branch
for branch in the_branches:
    asyncio.run(copy(branch))

    

