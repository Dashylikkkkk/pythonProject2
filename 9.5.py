m = int(input())
dishes = []
i = 0
j = 0
days = []
k = 0
for i in range(m):
    dishes.append(input())
n = int(input())
while j < n:
    o = int(input())
    j += 1
    s = 0
    while k < o:
        dishes_on = input()
        k += 1
        for i in range(len(dishes)):
            if dishes_on == dishes[i]:
                dishes.remove(dishes[i])
                break
print(*dishes, sep=' , ')
