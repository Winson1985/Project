# The codes are practices for basic Python learning
# Issued by Yongxing Qiu 2017/9/27
# Last modified 2017/12/29

# loop
nnode = 5
for inode in range (nnode):
    if inode == 2:
        break
print ("NodeIndex = " + str(inode))

# using lib
import random
for i in range(10):
    print(random.randint(20,22))

def PrintMessage():
    for i in range(1, 10):
        for j in range(1, 3):
            print("i = ", str(i), " j = ",str(j))
            if j == 2:
                continue
    return None

PrintMessage()

# print function
print("Hello", "World", sep="_", end = '||')
print("World", end = '\n')

# using math
import math
pi = math.pi
y = math.sqrt(pi)
print("y = ", y)

x = 20.0
y = math.pi / x

# using array
array = []
for i in range(0,8):
    array.append(i+1.0)
array.remove(2)
array.insert(2,11.1)

# using dictionary
list = {"A":1, "B":2, "C":3, "D":4}

print('list["A"] = ', list["A"])

key = "A"
if key in list:
    print(list.keys())
    print(list.values())

# The purpose of .get()
print(list.get("E", 0))
print(list["A"])

# Set default
list.setdefault("E", 5)
print(list.items())
list.setdefault("D", 3)
print(list.items())

sentence = " President Donald Trump said Wednesday that a lack of English \
             conversational skills on the part of Akie Abe, the wife of Prime \
             Minister Shinzo Abe, prompted him to leave his spot next to her at \
             dinner at an international summit and talk with Vladimir Putin instead."

count = {} # dict

for char in sentence:
    count.setdefault(char, 0)
    count[char] = count[char] + 1
print(count.items())
