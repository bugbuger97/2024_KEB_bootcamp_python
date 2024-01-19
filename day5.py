# 객체 지향 프로그래밍 규칙 : 확장은 열려있고, 수정은 닫혀있다. 즉 decorator는 기존의 코드를 바꾸지 않고 함수를 확장할 때 사용함.
# decorator : 하나의 함수를 취해서 또 다른 함수를 반환하는 함수임.
# decorator인 함수는 1. 함수 이름과 인수를 출력함 -> 2. 인수로 함수를 실행함. -> 결과를 출력함. -> 수정된 함수를 사용하도록 반환함.
def document_in(f):
    def new_func(*args,**kwargs):
        print('Running function :',f.__name__)
        print('Positional arguments :',args)
        print('Keyword arguments :',kwargs)
        result=f(*args,**kwargs)
        print('Result :',result)
        return result
    return new_func
@document_in
def power(n) -> int:
    '''
    거듭제곱
    :param n: 정수
    :return: 정수^2
    '''
    return pow(n,2)
@document_in
def Add(a,b) -> int:
    '''
    덧셈
    :param a: 정수 a
    :param b: 정수 b
    :return: a + b
    '''
    return a+b

print(Add(1,199))