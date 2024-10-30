nums=[5,8,11,12]
for x in range(len(nums)):
    if nums[x]%2==0:
        nums[x]='Even'
    else:
        nums[x]='Odd'
print(nums)