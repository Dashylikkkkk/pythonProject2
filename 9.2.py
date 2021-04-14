m = int(input())
i = 0
j = 0
k = 0
array = []
array_2 = []
while i < m:
    a = int(input())
    i += 1
    while j < a:
        array.append(input())
        j += 1
    j = 0
for i in range(len(array)):
    k = 0
    for j in range(len(array)):
        if array[i] == array[j]:
            k += 1
    if k == m:
        s = 0
        for q in range(len(array_2)):
            if array[i] == array_2[q]:
                s += 1
        if s == 0:
            array_2.append(array[i])
            print(array[i])
