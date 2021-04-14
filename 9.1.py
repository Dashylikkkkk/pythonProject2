m = int(input())
n = int(input())
book = []
list = []
i = 0
j = 0
k = 0
while i < m:
    a = input()
    book.append(a)
    i += 1
while j < n:
    b = input()
    list.append(b)
    j += 1
i = 0
for j in range(len(list)):
    k = 0
    for i in range(len(book)):
        if book[i] == list[j]:
            k += 1
    if k == 0:
        print('NO')
    else:
        print('YES')
