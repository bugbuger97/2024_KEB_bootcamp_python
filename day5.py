# positional argument : 인수 위치의 순서에 따라 인수가 들어갈 매개변수가 정해짐.
# keyword argument : 위치 인수의 혼란을 피하기 위해 매개변수에 상응하는 이름을 인수에 지정할 수 있다.
def AI(ML, DL): # positional argument
    return {'ML':ML,'DL':DL}
print(AI('Linear Regression', 'chat GPT'))

def AI(ML=None, DL='INDUCK'): # keyword argument
    return {'ML':ML,'DL':DL}
print(AI())

# 기본 인수는 함수가 실행될 때, 계산 되지 않고, 함수를 정의할 때, 계산됨.

def buggy(arg,result=[]): # argument 함수 괄호 안의 변수(외부)
    result.append(arg) # parameter 함수 내부 변수
    print(result)
buggy('A') # ['A']
buggy('B') # ['A', 'B']
# A, B가 리스트에 저장되어 있는 상태로 출력됨.
def nonbuggy(arg,result=None):
    if result is None:
        result=list()
    result.append(arg)
    print(result)
nonbuggy('A') # ['A']
nonbuggy('B') # ['B']