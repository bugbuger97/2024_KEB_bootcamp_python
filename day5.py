# generators : 반복자(iterators)을 위한 데이터의 자원이다. -> it keeps track of where it was the last time it was called and returns the next value.
# generator function : yield

def my_range(first=0, last=5, step =1):
    number = first
    while number < last:
        yield number
        number += step

r = my_range()
print(r,type(r))

for x in r: print(x)
for x in r: print(x) # 2번째에서는 아무것도 나오지 않는다. -> 한번 꺼내서 쓰면 남아 있지 않아서 똑같은 결과가 나오지 않는다.