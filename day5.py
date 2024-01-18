# generator(iterator에 대한 데이터의 소스로 자주 사용됨) : 시퀀스를 생성하는 객체, 전체 시퀀스를 한 번에 메모리에 생성하고 큰 시퀀스 순회 가능.
# range -> generator 중 하나
result=sum(range(1,101))
print(result)
# 제너레이터를 순회할 때마다 마지막으로 호출된 항목을 기억하고 다음 값을 반환함.

# generator founction : 일반 함수이지만, return문으로 값을 반환하지 않고 yield문으로 값을 반환함.
def my_range(first=10,last=0,step=-1):
    n = first
    while n > last:
        yield n # generator에서는 return 대신 yield를 씀.
        n += step

x = my_range()
print(x)
print(type(x))
for i in x:print(i)
for i in x:print(i) # nothing : 제너레이터는 한번만 순회할 수 있음. (값을 기억이나 저장하지 않음)

# generator comprehensions
# Generator = (i for i in [1,2,3,4,5,6])
# Generator = (i for i in range(1,10))
Generator = (i for i in zip([1,2,3,4,5],[2,4,8,16,32]))
print(type(Generator))
print(Generator)
for i in Generator:
    print(i)