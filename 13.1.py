n = int(input())
items = [''] * n
for i in range(n):
    items[i] = input()
n = int(input())
for i in range(n):
    amountLeft = int(input())
    itemsTemp = [''] * amountLeft
    for j in range(amountLeft):
        number = int(input())
        for k in range(len(items)):
            if number == k + 1:
                itemsTemp[j] = items[k]
    items = itemsTemp.copy()
print(*items, sep='\n')
