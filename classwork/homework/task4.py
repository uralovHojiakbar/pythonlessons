def every_nth_element(string, num):
    lst2 = []
    for i in range(num - 1, len(string), num):
        lst2.append(string[i])
    return lst2

string = [10, 20, 30, 40, 50, 60, 70]
print(every_nth_element(string, 2))
