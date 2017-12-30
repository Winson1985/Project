# The codes are practices for basic Python learning
# Issued by Yongxing Qiu 2017/9/27
# Last modified 2017/12/29

# list
list = []
for i in range(0, 12, 2):
    list.append(i*1.0)
print("Orignal List:")
print(list)

# remove
list.remove(2)
print("Removed list[2]:")
print(list)

# insert
list.insert(4,1.0)
print("Inserted memb into list[4]:")
print(list)

# remove
list.remove(1.0);   
print("Removed memb of 1.0")
print(list)

# pop memb
popped_list_memb = list.pop(2)
print("Popped member:")
print(popped_list_memb)

print("Changed List:")
print(list)

# permanent sorting list
list.sort()
print("Permanent Sorting:")
print(list)
# permanent reverse sorting list
list.sort(reverse = True)
print("Permanent Reverse Sorting:")
print(list)

# temporary sorting
print("Temporary Sorting:")
print(sorted(list))
print(list)

# length of list
print("Length of list:")
print(len(list))

# erogodic list
for memb in list:
    print(str("memb: " + str(memb)))

# list parsing
list2 = [memb*2.0 for memb in list]
print("list2:")
print(list2)


# List reference, copy
print("Reference")
a = [1, 2, 3]
print("Original Value")
b = a
print("a = ", a)
print("b = ", b)

print("Modified Value -- Reference")
a.insert(1, 0.0)
print("a = ", a)
print("b = ", b)

print("Copy")
a = [1, 2, 3]
print("Original Value")
b = a.copy()
print("a = ", a)
print("b = ", b)

print("Modified Value -- Copy")
a.insert(1, 0.0)
print("a = ", a)
print("b = ", b)

print(":")
a = [1, 2, 3]
print("Original Value")
b = a[:]
print("a = ", a)
print("b = ", b)

print("Modified Value -- :")
a.insert(1, 0.0)
print("a = ", a)
print("b = ", b)

# include other lib
import sys

sys.path.append('C:\\Users\\qiuyo\\Documents\\Projects\\Codes\\Project\\Project\\PracticesPy\\PythonLearning\\PythonLearning')

import funcs as f

dampingratio = f.LogDamp2DampRatio(0.001/100)*100
print("dampingratio = ", dampingratio)
logdamp = f.DampRatio2LogDamp(1/100.0)*100
print("logdamp = ", logdamp)

