# two asterisks (**) -> 딕셔너리로 취급함.
def print_kwargs(**kwargs):
    print('Keyword argument :',kwargs)

print_kwargs() # {} -> dict

# 인수의 순서에 대한 우선 순위 : positional arguments > *args > **kwargs

# help(len) == print(len.__doc__)
print(len.__doc__)

# 파이썬은 모든 것이 객체이다.

def squares(n):
    return n*n

def run_function(f,number):
    return f(number)

print(squares(7))
print(run_function(squares,9))

# 함수 안에 인수가 몇 개가 올지 예측이 되지 않을 떄는 가변 매개변수를 쓰는 것이 좋다.
def n_squares(*n) -> list: # n == tuple type
    '''
    넘겨 받은 수치 데이터들의 거듭 제곱 값을 리스트에 담아서 리턴
    :param n: tuple
    :return: list
    '''
    return [i*i for i in n]
    #return n*n

def n_run_function(f,*number) -> list:
    return f(*number)

print(*n_squares(8,2,3,9,5)) # 64 4 9 81 25
print(n_run_function(n_squares,9,10))