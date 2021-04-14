n = int(input())
i = 0
while i < n:
    s = input()
    i += 1
    if s[:2] == '%%':
        print(s[2:])
    elif s[:4] == '####':
        s = s
    else:
        print(s)
