dic = {'a': 1, 'b': 2, 'c': 3}
dic1 = {}
for x,y in zip(dic, dic.keys()):
    dic1[dic[x]] = y

print(dic1)