# 실행 : Ctrl + Shift + F10
# Mutable : list, Bytearray, Set, Dictionary -> 값의 변화가 있을 수 있음.

univ = "Inha university"
print(univ)
print(univ[5])
# univ[5] = 'U' # Unmautable -> 문자열은 값을 고칠 수 없다.
# print(univ)
subject = ['python', 'c++', 'linux', 'data structure', 'database']
print(subject)
print(subject[3])
subject[3] = 'data structure & algorithm' # Matuble
print(subject)

# print(0.1)
# print(1e-1)
# print(0.01)
# print(1e-2)
# print(3.14)
# print(314e-2)
# print(3.141592)
# print(3141592e-6)
# print(0.3141592e1)

# literal : 메모리 자체의 값을 의미
# 91 = 71 -> SyntaxError: cannot assign to literal here.

# 변수명 표기
# help('keywords')에 있는 것은 변수명으로 사용할 수 없음. -> reserved words
# 변수명이 숫자 먼저 시작할 수 없다.
# 언더바는 어디에 있든 가능함.
# 변수명을 만들 때, 특수 기호는 _만 가능함.

# money = 5,000,000 # , : tuple
# print(money)
# print(type(money)) # tuple
#
# cash = 5_000_000
# print(cash)
# print(type(cash))

base_number = int(input('Input base number : '))
exponent_number = int(input('Input exponent number : '))
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number**exponent_number}')