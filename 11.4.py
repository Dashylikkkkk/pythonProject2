n = int(input())
array = []
for i in range(n):
    s = input()
    str = ''
    check = False
    char = ''
    if s[0] == ' ':
        space = True
    else:
        space = False
    for j in s:
        if j == "'" and not check:
            check = True
        elif j == "'" and check and char != "\\":
            check = False
        if j != ' ' and char == ' ':
            space = False
            str += j
        elif j == ' ' and space and not check:
            str += j
        elif j == '#' and not check:
            break
        elif j == ' ' and char == ' ':
            pass
        else:
            str += j
        char = j
    array.append(str)
for i in array:
    print(i)
