n = int(input())
m = int(input())
array = []
array_2 = []
for i in range(n):
    array.append(input())
for i in array[::2]:
    array_2.append(i[::2])
for i in array_2:
    print(i)
