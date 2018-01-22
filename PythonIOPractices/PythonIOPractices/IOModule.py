# The code is used to practise Python I/O programming
# Issued by Yongxing.Qiu 2018/01/04
# Last modified 2018/01/04

def LoadInFloatList(string):
    import re
    if len(string) > 0:
        list = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',string)
        data_list = []
        for data in list:
            data = float((data[0]+data[2]))
            data_list.append(data)
        return data_list