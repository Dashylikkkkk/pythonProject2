num = int(input())
s = input()
answer = ''
for i in s:
    if (ord(i) + num) > 1103 and 1039 < ord(i) < 1104:
        i = chr(1040 + (ord(i) + num - 1103))
    elif (ord(i) + num) < 1040 and 1039 < ord(i) < 1104:
        i = chr(1103 - (1040 - (ord(i) + num)))
    elif 1039 < ord(i) < 1104:
        i = chr(ord(i) + num)
    answer += i
print(answer)
