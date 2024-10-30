def double_check(lists):
    list1 = []
    for x in lists:
        if x not in list1:
            list1.append(x)
    return list1

lists = ['apple', 'banana', 'apple', 'orange', 'banana']
print(double_check(lists))