nums = [1, 3, 5, 6]
target = 5
index = 0
for i in range(len(nums)):
    if nums[i] == target:
        index = i
        break
    elif nums[i] < target:
        index = i + 1
print(index)



