n = int(input())
array = []
array_2 = []
for i in range(n):
    array.append(input())
n_2 = int(input())
while len(array) > 0:
    for i in range(len(array)):
        if i == 0 or i % n_2 == 0:
            array_2.append(i)
    for i in range(len(array_2)):
        print(array[array_2[i] - i])
        array.pop(array_2[i] - i)
