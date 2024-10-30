dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'b': 10, 'c': 20, 'd': 30}
copy = set()
for x, in zip(dic1 .keys()):
    if x in dic2.keys():
        copy.add(x)

print(copy)