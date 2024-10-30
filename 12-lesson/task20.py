my_list = [10, 20, 30]
my_tuple = [40, 50, 60]
num = my_list[0]
my_list[0] = my_tuple[0]
lst = list(my_tuple)
lst[0] = num
my_tuple = tuple(lst)
print(my_list)
print(my_tuple)