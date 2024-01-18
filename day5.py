# 매개변수(parameter) : 함수의 정의에서 전달받은 인수를 함수 내부로 전달하기 위해 사용하는 변수를 의미함.
# 인수(argument) : 함수가 호출될 때 함수로 값을 전달해주는 값임.

def my_print(sometihing): # something -> 매개변수(parameter)
    print(sometihing + ' ' + sometihing)

my_print('Inha University') # 'Inha University' -> 인수(argument)

# 함수 외부에서는 인수라고 하지만 내부에서는 매개변수하고 함.