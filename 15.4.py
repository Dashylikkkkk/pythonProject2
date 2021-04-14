n = int(input())
array_num = []
array_med = []
array_moda = []
str = ''
for i in range(n):
    array_num.append(input())
for i in range(len(array_num)):
    str += " " + array_num[i]
    array_med.append(array_num[i].split()[len((array_num[i].split())) // 2])
    answer = 0
    signTemp = 0
    numberTemp = 0
    numberMax = 0
    for j in range(len(array_num[i].split())):
        signTemp = array_num[i].split()[j]
        numberTemp = 0
        for k in range(len(array_num[i].split())):
            if array_num[i].split()[j] == array_num[i].split()[k]:
                if numberTemp == 0:
                    numberTemp += 2
                else:
                    numberTemp += 1
        if numberTemp > numberMax:
            numberMax = numberTemp
            answer = signTemp
    array_moda.append(answer)
for i in range(len(array_med)):
    print(array_med[i], ' ', end='')
print('')
for i in range(len(array_moda)):
    print(array_moda[i], ' ', end='')
print('')
print(array_med[len(array_med) // 2])
numberMax = -9999
for i in range(len(array_moda)):
    signTemp = array_moda[i]
    numberTemp = 0
    for j in range(len(array_moda)):
        if array_moda[i] == array_moda[j]:
            numberTemp += 1
    if numberMax < numberTemp:
        answer = signTemp
        numberMax = numberTemp
print(answer)
print(str[len(str) // 2])
numberMax = -9999
for i in range(len(str.split())):
    signTemp = str.split()[i]
    numberTemp = 0
    for j in range(len(str.split())):
        if str.split()[i] == str.split()[j]:
            numberTemp += 1
    if numberMax < numberTemp:
        answer = signTemp
        numberMax = numberTemp
print(answer)
