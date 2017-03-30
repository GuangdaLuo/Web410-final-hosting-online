#!C:\Python27\python.exe







# change python interpreter path for all python files in this directory.
#
# The method to do the replacement is very shitty; but it works.


import os
import sys
import re

py_path = "#!C:\Python27\python.exe\n\n"

if sys.argv[1] == "mac":
    py_path = "#!/usr/bin/python\n"
else:
    py_path = "#!C:\Python27\python\n"

# print os.listdir(os.curdir)

for file_name in os.listdir(os.curdir):
    if re.search("\.py", file_name) is not None:
        # find a .py file
        target_file = open(file_name, "r")
        file_content = target_file.readlines()
        target_file.close()
        file_content[0] = py_path
        target_file = open(file_name, "w")
        for line in file_content:
            target_file.write(line)
        target_file.close()
    
