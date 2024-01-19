# 데코레이터를 여러 개를 붙일 수 있음.

# Recursion
def factorial_repetition(n) -> int:
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result

def factorial_recursion(n) -> int:
    '''
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수
    :return: function, int
    '''
    if n == 1:
        return n
    else:
        return n*factorial_recursion(n-1)

print(factorial_repetition(5))
print(factorial_recursion(6)) # 재귀는 반복문보다 속도가 느리다