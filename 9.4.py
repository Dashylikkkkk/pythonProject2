m = int(input())
i = 0
j = 0
k = 0
s = 0
items = []
done = []
while i < m:
    items.append(input())
    i += 1
n = int(input())
while j < n:
    recipes = input()
    j += 1
    products = int(input())
    s = 0
    k = 0
    while k < products:
        items_in = input()
        k += 1
        for i in range(len(items)):
            if items_in == items[i]:
                s += 1
    if s == products:
        done.append(recipes)
for i in range(len(done)):
    print(done[i])
