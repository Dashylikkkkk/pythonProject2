s = input()
a = None
b = 0
for i in s:
    if a != i:
        if b > 0:
            print(b, a)
        a = i
        b = 1
    else:
        b += 1
print(b, a)

