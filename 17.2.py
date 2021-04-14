n = int(input())
nums = []
nums_2 = []
for i in range(n):
    nums.append(input())
n = int(input())
for i in range(n):
    names = input()
    str = ''
    for j in range(len(nums)):
        if nums[j].split()[1] == names:
            str += nums[j].split()[0] + ''
    if str != '':
        nums_2.append(str)
    else:
        nums_2.append('Нет в телефонной книге')
for i in range(len(nums_2)):
    print(nums_2[i])
