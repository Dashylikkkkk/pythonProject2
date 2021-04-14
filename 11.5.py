s = input()
a = len(s)
while a >= 2:
    print(s[1:(a - 1)])
    s = s[1:(a - 1)]
    a -= 2
