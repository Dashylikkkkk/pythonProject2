n = input()
a = input().split()
for i in a:
    if n.upper() in i or n.lower() in i:
        print(i)
