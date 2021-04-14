s = input()
n = int(input())
b = input()
if 0 < n <= len(s) and s[n - 1] == b and len(b) == 1:
    print('ДА')
elif 0 < n <= len(s) and s[n - 1] != b and len(b) == 1:
    print('НЕТ')
else:
    print('ОШИБКА')

