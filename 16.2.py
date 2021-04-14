n = int(input())
s = []
s_2 = []
for i in range(n):
    s.append(input())
r = int(input())
for i in range(r):
    num = input()
    num = num.split(',')
    a = int(num[0])
    b = int(num[1])
    s_2.append(s[a].split(',')[b])
for i in range(len(s_2)):
    print(s_2[i])
