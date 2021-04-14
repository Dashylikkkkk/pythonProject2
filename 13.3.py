a = []
n = int(input())
for i in range(n):
    b = 0
    for j in range(len(a)):
        if a[j] == a[- 1 - j]:
            b += 1
    a.append(b)
del a[-1]
for i in a:
    print(i)
