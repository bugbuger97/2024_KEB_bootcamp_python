# Inner function(내부 함수) : 반복문이나 코드 중복을 피하고자 또 다른 함수 내에 어떤 복잡한 작업을 1번 이상 수행할 때 유용하게 사용됨.
def Out(a,b):
    def In(c,d):
        return c+d
    return In(a,b)
print(Out(10,19))

# Closure(클로저) : 다른 함수에 의해 동적으로 생성되는데, 외부 함수로부터 생성된 변수값을 변경하고, 저장할 수 있는 함수임.
# 어떤 함수의 내부 함수가 외부 함수의 변수를 참조할 때, 외부 함수가 종료된 후에도 내부 함수가 외부 함수의 변수를 참조할 수 있도록 어딘가에 저장하는 함수임.
def script(saying):
    def In():
        return f'{saying} : I want to go home!!!!!!'
    return In
I = script('INHA') # 클로저 생성
ME = script('ME')
print(I)
print(I())
print(type(I))

print('\n')

print(ME)
print(ME())
print(type(ME))
# 클로저 조건 : 1. 어떤 함수는 내부 함수를 가질것, 2. 그 내부 함수가 외부 함수를 참조할 것, 3. 외부 함수가 내부 함수를 리턴할 것.
# 클로저를 쓰는 이유 : 전역변수의 남용 방지를 위해서