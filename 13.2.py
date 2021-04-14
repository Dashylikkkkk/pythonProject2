array = []
i = 0
n = int(input())
while i < n:
    array.append(int(input()))
    i += 1
array.sort()
array.reverse()
for i in range(len(array)):
    print(array[i])
