n = int(input())
i = 0
array = []
while i < n:
    a = input()
    b = int(input())
    i += 1
    c = str(a) + ' ' + str(b)
    array.append(c)
array.reverse()
for i in range(len(array)):
    print(array[i])
