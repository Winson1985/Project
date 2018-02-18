from random import randint

# List Parsing
list = [randint(-10,10) for i in range(12)]
print("list: " + str(list))
x2 = [x for x in list if x >= 0]
print("x2: " + str(x2))

# Dictionary Parsing
dict = {k:randint(-10,10) for k in range(12)}
print("dict: " + str(dict))
d2 = {k:v for k,v in dict.items() if v >= 0}
print("d2: " + str(d2))

# Collection Parsing
collection = set(list)
print("collection: " + str(collection))
c2 = {x for x in collection if x >= 0}
print("c2: " + str(c2))

# Def name of member of tuple
# (type, version, solver)
numspan = 12
span = [x for x in range(12)]
name = 'alpha_blade'

blade = (numspan, span, name)

print("blade: " + str(blade))

from collections import namedtuple
Blade = namedtuple('Blade', ['num_span', 'span', 'name'])
b = Blade(numspan, span, name)
print("b.num_span: " + str(b.num_span))
print("b.span: " + str(b.span))
print("b.name: " + str(b.name))

from module1 import *

string = "Hello World"
obj_list = []
for i in range(0,10):
    str1 = string + str(i)
    obj = Display(str1)
    obj_list.append(obj)

print(obj_list)

obj_list[3].display()

obj_super = SuperDisplay("This is a super class obj")
obj_super.display()

obj_super.weapon.fire()


import re
string = "   'B1 Mx (Root Axes)' 'B2 Mx (Root Axes)' 'B3 Mx (Root Axes)'  "
str_list = string.strip().split("' '")
str_list2 = []
for str in str_list:
    char_list = re.findall("[^']", str)
    str = ""
    str = str.join(char_list)
    str_list2.append(str)

print(str_list2)



dict = {'B1 Mx (Root Axes)' : 'Col1', \
        'B2 Mx (Root Axes)' : 'Col2', \
        'B3 Mx (Root Axes)' : 'Col3'}

print(dict['B2 Mx (Root Axes)'])

