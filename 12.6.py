s = input()
a = [' *   ', '* *  ', '***  ', '* *  ', '* *  ']
b = ['**   ', '* *  ', '**   ', '* *  ', '**   ']
c = [' *   ', '* *  ', '*    ', '* *  ', ' *   ']
for j in range(5):
    for i in range(len(s)):
        if s[i] == 'A':
            print(a[j], end='')
        elif s[i] == 'B':
            print(b[j], end='')
        elif s[i] == 'C':
            print(c[j], end='')
    print()
