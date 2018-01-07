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
num_span = 12
span = [x for x in range(12)]
name = 'alpha_blade'

blade = (num_span, span, name)

print("blade: " + str(blade))

from collections import namedtuple
Blade = namedtuple('Blade', ['num_span', 'span', 'name'])
b = Blade(num_span, span, name)
print("b.num_span: " + str(b.num_span))
print("b.span: " + str(b.span))
print("b.name: " + str(b.name))





