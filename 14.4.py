n = input()
z = '*'
array_num = []
max = -9999
for i in range(len(n)):
    if i % 2 == 0:
        if max < int(n[i]):
            max = int(n[i])
        array_num.append(int(n[i]))
width = len(array_num) + 2
height = max + 2
for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1:
            print(z, end='')
        elif j == 0 or j == width - 1:
            print(z, end='')
        elif height - i <= array_num[j - 1]:
            print(z, end='')
        else:
            print(' ', end='')
    print('')
