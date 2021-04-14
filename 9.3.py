n = int(input())
i = 0
s = 0
array = []
array_2 = []
while i < n:
    array.append(input())
    array_2.append(False)
    i += 1
for i in range(len(array)):
    k = 0
    for j in range(len(array)):
        s = 0
        if array[i] == array[j] and i != j:
            array_2[i] = True
    if array_2[i] == True:
        s += 1
print(s)
