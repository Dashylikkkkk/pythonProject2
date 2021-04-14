s = input()
s_eng = ''
eng = ''
for i in range(len(s)):
    rus = s[i]
    if rus.lower() == 'а':
        eng = 'a'
    elif rus.lower() == 'б':
        eng = 'b'
    elif rus.lower() == 'в':
        eng = 'v'
    elif rus.lower() == 'г':
        eng = 'g'
    elif rus.lower() == 'д':
        eng = 'd'
    elif rus.lower() == 'е' or rus.lower() == 'ё':
        eng = 'e'
    elif rus.lower() == 'ж':
        eng = 'zh'
    elif rus.lower() == 'з':
        eng = 'z'
    elif rus.lower() == 'и' or rus.lower() == 'й':
        eng = 'i'
    elif rus.lower() == 'к':
        eng = 'k'
    elif rus.lower() == 'л':
        eng = 'l'
    elif rus.lower() == 'м':
        eng = 'm'
    elif rus.lower() == 'н':
        eng = 'n'
    elif rus.lower() == 'о':
        eng = 'o'
    elif rus.lower() == 'п':
        eng = 'p'
    elif rus.lower() == 'р':
        eng = 'r'
    elif rus.lower() == 'с':
        eng = 's'
    elif rus.lower() == 'т':
        eng = 't'
    elif rus.lower() == 'у':
        eng = 'u'
    elif rus.lower() == 'ф':
        eng = 'f'
    elif rus.lower() == 'х':
        eng = 'kh'
    elif rus.lower() == 'ц':
        eng = 'tc'
    elif rus.lower() == 'ч':
        eng = 'ch'
    elif rus.lower() == 'ш':
        eng = 'sh'
    elif rus.lower() == 'щ':
        eng = 'shch'
    elif rus.lower() == 'э':
        eng = 'e'
    elif rus.lower() == 'ю':
        eng = 'iu'
    elif rus.lower() == 'я':
        eng = 'ia'
    elif rus.lower() == 'ы':
        eng = 'y'
    elif rus.lower() == 'ь' or rus.lower() == 'ъ':
        rus = ''
    if rus.isupper() and eng != '':
        rus = eng[0].upper() + eng[1:len(eng)]
    if eng != '':
        s_eng += eng
    else:
        s_eng += rus
print(s_eng)
