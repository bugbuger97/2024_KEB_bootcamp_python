# 파이썬에서는 오버로딩을 지원하지 않는다.
def a(n1,n2):
    print(n1,n2)
def a(n):
    print(n)

a(1) # 1
#a(1,2) # TypeError: a() takes 1 positional argument but 2 were given

def b(n):
    if n is None:
        print(f'{n} is None')
    elif n:
        print(f'{n} is True')
    else:
        print(f'{n} is False')

b([]) # False
b([0]) # True
b(0) # False
b(None) # None
b('') # False