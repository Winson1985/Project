# The code is used to practise Python I/O programming
# Issued by Yongxing.Qiu 2018/01/04
# Last modified 2018/01/04

import sys
sys.path.append('D:\\MyWork\\MyProject\\MBDX\\Source\\Repos\\Trainning\\ \
                 PythonIO\\PythonIO')

filepath = 'folder\\sample.inp'

# open and read all of contents of file
with open(filepath, 'r') as file_obj:
    contents = file_obj.read()
    print(contents)

# method1: read each line of the file
lines = []
with open(filepath, 'r') as file_obj:
    for line in file_obj:
        lines.append(line.rstrip()) # rstrip() removes \n

print(lines)

# method2: read each line of the file
lines = []
with open(filepath, 'r') as file_obj:
    lines = file_obj.readlines()
    for line in lines:
        print(line.rstrip())

# removes LHS space and \n
new_lines = []
for line in lines:
    line = line.strip()  # removes LHS space
    new_lines.append(line)
print(new_lines)

# write output file
ouppath = 'folder\\sample.out'
with open(ouppath, 'w') as file_obj:
    for line in lines:
        file_obj.write(line)
print("Write output finished!")

# add new content in written output file
ouppath = 'folder\\sample.out'
with open(ouppath, 'a') as file_obj:
    for line in new_lines:
        file_obj.write(line)
print("Write output finished!")

# file I/O using JSON
import json
outfile = 'folder\\sample.json'
with open(outfile, 'w') as file_obj:
    json.dump(lines, file_obj)

# load into list
file = outfile
str_list = []
with open(file, 'r') as file_obj:
    str_list = json.load(file_obj)
print(str_list)

# Re for string I/O
import re

from IOModule import *

a = []
a = LoadInFloatList(lines[0])

# find a string
s = "absoutly: 23.45"
print(s.find("23.45"))

s = '  WINDF  "D:\\MyWork\\MyProject\\MBDX\\Model\\winds\\tw12_80hh_s276.wnd"'
# method 1
str_list = re.findall('([^"]*)', s)
print(str_list)

# method 2
path = s.split('"')[1]
print(path)

# Exceptions
ouppath = 'folder1\\sample.out'
try:
    with open(ouppath, 'a') as file_obj:
        for line in new_lines:
            file_obj.write(line)
except FileNotFoundError:
    print("file not existed!")
else:
    print("Write output finished!")


