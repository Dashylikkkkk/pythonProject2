url = input()
get = input()
get = url.find(get) + len(get) + 1
answer = ''
while url[get] != '?' and url[get] != '&' and url[get] != '=' and url[get] != '#' and get != len(url)-1:
    answer += url[get]
    get += 1
    if get == len(url)-1:
        answer += url[get]
print(answer)
