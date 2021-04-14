m = int(input())
i = 0
j = 0
list_white = []
list = []
k = []
while i < m:
    list_white.append(input())
    i += 1
n = int(input())
while j < n:
    list.append(input())
    j += 1
for i in range(len(list)):
    for j in range(len(list_white)):
        if list[i] == list_white[j]:
            print(list[i])
