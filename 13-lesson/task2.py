dic={'apple': 10, 'banana': 15, 'cherry': 8}
new_dic=max(dic, key=dic.get)
print(new_dic)