# is라는 문법을 이용해서 False와 None을 구분할 수 있다.
thing = None  # False
if thing is None:
    print('thing is Nothing')
else:
    print('thing is something')

# Positional Arguments -> def f(x,y) : 순서에 관계가 있다.
# Keyword Arguments -> def f(x=None,y=1)

def buggy(arg, result = []):
    result.append(arg)
    print(result)
buggy(1) # [1]
buggy(2) # [1, 2] -> 계속 1이 들어가 있다.

def nonbuggy(arg, result = None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
nonbuggy(1) # [1]
nonbuggy(2) # [2] -> 겹쳐지지 않는 것을 볼 수 있다.

# 가변 인수
def args(*arg):
    print('positional tuple :',arg)
args(1) # 함수의 매개변수에 애스터 리스크(*)를 사용할 때, 애스터 리스크(*)는 매개변수에서 위치 인수 변수를 튜플로 묶음.