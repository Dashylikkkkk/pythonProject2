i = 0
n = int(input())
level_1 = []
level_2 = []
j = 0
while i < n:
    pvp = int(input())
    level_1.append(pvp)
    level_2.append(pvp)
    i += 1
num = int(input())
while j < num:
    bro = int(input())
    index = int(input())
    plus = int(input())
    if bro == 1:
        level_1[index] += plus
    elif bro == 2:
        level_2[index] += plus
    j += 1
k = 0
i = 0
j = 0
for i in range(len(level_2)):
    if level_1[i] == level_2[i]:
        k += 1
print(*level_1)
print(*level_2)
print(k)


