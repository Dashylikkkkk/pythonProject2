a = input()
n = int(a[0:4])
sum = int(a[4:])
i = 0
summa = 0
array = []
while i < n:
    b = input()
    c = int(b[0:7])
    d = int(b[8:12])
    e = int(b[13:])
    price = c * d
    if price != e:
        array.append(i + 1)
    summa = summa + c * d
    i += 1
    c = d = e = 0
print((sum - summa))
print(*array)





