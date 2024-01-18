# 독스트링 : 함수의 가독성을 위해 작성하는 것임.
def squares(n) -> int:
    '''
    제곱 함수
    :param n: 정수형 숫자
    :return: (정수형 숫자)^2
    '''
    return n*n

help(squares)
print(squares.__doc__) # docstring