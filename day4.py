# dict : mutable
acme_customer = dict(first='Wile',second='E',last='Coyote') # key에 예약어 같은 이름을 넣을 수 없다.
print(acme_customer)

lol = [[1,2],[3,4],[5,6]]
print(dict(lol))

lol = ([1,2],[3,4],[5,6])
print(dict(lol))

lol = ['ab','cd','ef']
print(dict(lol))