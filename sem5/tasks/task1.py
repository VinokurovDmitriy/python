with open('task1.txt', 'r') as f:
    file_str = f.read()
nums = file_str.split(' ')
print(nums)
for index in range(len(nums)):
    if int(nums[index]) - 1 != int(nums[index - 1]):
        print(nums[index])
