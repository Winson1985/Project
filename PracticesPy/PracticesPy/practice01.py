

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

sentence = " President Donald Trump said Wednesday that a lack of English conversational skills on the part of Akie Abe, the wife of Prime Minister Shinzo Abe, prompted him to leave his spot next to her at dinner at an international summit and talk with Vladimir Putin instead."

count = {} # dict

for char in sentence:
    count.setdefault(char, 0)
    count[char] = count[char] + 1
print(count.items())


# -*- coding= utf-8 -*-
#copyRight by OSCAR
import functools
#定义文件读取函数，并且输出元素为词频的字典
def readFile(file_name):
    y = []
    with open(file_name, 'r',encoding="utf8") as f:
        x=f.readlines()
    for line in x:
        y.extend(line.split())
    word_list2 = []

    # 单词格式化：去掉分词之后部分英文前后附带的标点符号
    for word in y:
        # last character of each word
        word1 = word

        # use a list of punctuation marks
        while True:
            lastchar = word1[-1:]
            if lastchar in [",", ".", "!", "?", ";", '"']:
                word2 = word1.rstrip(lastchar)
                word1 = word2
            else:
                word2 = word1
                break

        while True:
            firstchar = word2[0]
            if firstchar in [",", ".", "!", "?", ";", '"']:
                word3 = word2.lstrip(firstchar)
                word2 = word3
            else:
                word3 = word2
                break
                # build a wordList of lower case modified words
        word_list2.append(word3)
    #统计词频
    tf = {}
    for word in word_list2:
        word = word.lower()
            # print(word)
        word = ''.join(word.split())
        if word in tf:
            tf[word] += 1
        else:
            tf[word] = 1
    return tf

def get_counts(words):
    tf = {}
    for word in words:
        word = word.lower()
        # print(word)
        word = ''.join(word.split())
        if word in tf:
            tf[word] += 1
        else:
            tf[word] = 1


#合并两个字典的方法1
def merge1(dic1, dic2):
    for k, v in dic1.items():
        if k in dic2.keys():
            dic2[k] += v
        else:
            dic2[k] = v
    # print(dic2)
    return dic2

#合并两个字典的方法2
def merge2(dic1, dic2):
    from collections import Counter
    counts = Counter(dic1) + Counter(dic2)
    return counts

#获得前n个最热词和词频
def top_counts(word_list,n=10):
     value_key_pairs = sorted([(count, tz) for tz, count in word_list.items()],reverse=True)
     return value_key_pairs[:n]
     # print(value_key_pairs[:n])
 
file_list = [r'C:\Users\qiuyo\Documents\Visual Studio 2017\Projects\PythonPrcatices\paper.txt']

cc=map(readFile,file_list)
word_list = functools.reduce(merge2,cc)
top_counts=top_counts(word_list)
# print(top_counts)
print ("最常用的单词排行榜:")
for word in top_counts[0:10]:
    print("{0:10}{1}".format(word[1], word[0]))