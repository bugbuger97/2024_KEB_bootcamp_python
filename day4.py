# comprehension
rows = range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]
print(cells)
print(type(cells))

cells = ((row,col) for row in rows for col in cols)
print(cells)
print(type(cells))

# iterable는 member를 하나씩 차례로 반환 가능한 object를 의미한다.
# iterator는 next() 메소드로 데이터를 순차적으로 호출 가능한 object이다.

'''
제너레이터는 발전기라는 의미처럼 이 객체를 호출할 때마다 yeild가 작동되 값을 순차적으로 산출함.
함수 내부에서 yield가 사용하면 그 함수는 제너레이터가 되며, 제너레이터는 이터레이터를 생성해주는 함수임.
이터레이터는 클래스에 iter, next 등의 메서드를 구현해야 하지만 제너레이터는 함수 안에서 yield라는 키워드만 사용하면 손쉽게 생성할 수 있다는 장점이 있음.
yield로 생성된 제너레이터는 이미 iter와 next를 갖고 있는 것을 아래와 같이 확인할 수 있음.
'''
print(cells.__next__())
print(cells.__next__())
print(cells.__next__())
print(cells.__next__())