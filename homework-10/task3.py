def max_more_than_one(lst):
    lst.sort()
    lst.reverse()
    for x in lst:
        if lst.count(x) > 1:
            return x
    return 'None'

list1 = [1,1,2,2,3,3,4,5,4,3,5,6,7]
print(max_more_than_one(list1))