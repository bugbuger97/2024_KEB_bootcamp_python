def get_odds(n):
    for i in range(1,n+1,2):
        yield i

cnt = 0
odds = get_odds(9)
for odd in odds:
    cnt+=1
    if cnt == 3:
        print(f'Third number is {odd}')
        break
for odd in odds:
    cnt+=1
    if cnt == 3:
        print(f'Third number is {odd}') # 제너레이터는 한 번밖에 나오지 않기 때문에 출력 되지 않는다.
        break