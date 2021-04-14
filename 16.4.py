n = int(input())
table = [[-1] * n for i in range(n)]
for i in range(1, n):
    text = input()
    for j in range(len(text.split())):
        table[i][j] = int(text.split()[j])
first = input()
second = int(first.split()[1])
first = int(first.split()[0])
minim = 999999
minTemp = -2
number = first
checker = 0
while checker < n * n + 1:
    for i in range(n):
        if table[i][first] != -1 and table[i][first] < table[second][first]:
            for j in range(n):
                if table[i][j] != -1:
                    minTemp = table[i][first] + table[j][i]
                    if minTemp < minim:
                        minim = minTemp
                        number = i
    checker += 1
print(number)
