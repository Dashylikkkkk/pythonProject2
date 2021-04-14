n = int(input())
array = []
for i in range(n):
    s = input()
    if 'лук' not in s:
        array.append(s)
print(', '.join(array))
