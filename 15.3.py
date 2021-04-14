s = input().upper()
j = 0
for i in range(0, len(s)):
    if s.count(s[i]) > j:
        j = s.count(s[i])
print(j)
