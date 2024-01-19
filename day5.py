# 9.1
def good(*args):
    List=list(args)
    print(List)
    return List
good('Harry','Ron','Hermione')

# 9.2
def gets_odds():
    odds = [i for i in range(10) if i%2==1]
    for i in odds:
        yield i
something = gets_odds()
print(something)
cnt=0
for i in something:
    cnt+=1
    if cnt == 3:
        print(f'세번째 홀수 : {i}')

# 9.3
def test(f):
    def inner(*args):
        print('Start')
        print(f(*args))
        print('end')
    return inner
@test
def my_int_print(a):
    return a

my_int_print(1)