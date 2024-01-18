# Variable length Arguments (가변 인수) : 파이썬에서는 함수에서 입력값이 몇 개가 될지 모를 때을 위해 가변 인수를 튜플 타입으로 제공함.
# *args : 앞에 애스터리스크(*)를 붙여주는 것이 특징이다.
def print_Variable_length_Arguments(*args):
    print('Positional tuple :',args)
print_Variable_length_Arguments(1,2,3,4,5)
# *args는 함수 외부에서 여러 개로 이루어진 값들을 함수 내부에 튜플 형태로 모은다.

# Variable length keyword Arguments (가변 키워드 인수) : 키워드 인수를 딕셔너리로 묶기 위해 2개의 애스터리스크(**)를 사용하여, 인수의 이름은 key, 이 key에 대응하는 딕셔너리 값이 value임.
def print_Variable_length_keyword_Arguments(**kwargs):
    print('Keyword arguments :',kwargs)
print_Variable_length_keyword_Arguments()
print_Variable_length_keyword_Arguments(university='inha')
# 함수 외부에서 **kwargs는 딕셔너리 kwargs를 '이름=값' 인수로 분해함.
# 함수 내부에서 **kwargs는 '이름=값' 인수를 단일 딕셔너리 매개변수 kwargs에 모은다.

# 키워드 전용 인수 : 값을 위치적으로 제공하지 않고, '이름=값'으로 제공해야함.
def my_print_data(data,*,start=0,end=100): # 함수 정의에서 단일 애스터리스크(*)는 start 및 end 매개변수의 기본값을 사용하고 싶지 않은 경우, 명명된 인수로 제공해야 함.
    for value in (data[start:end]):
        print(value)
data = [0,1,2,3,4,5,6,7,8]
# my_print_data(data)
# my_print_data(data,start=5)
my_print_data(data,end=4)
# 함수에 인수를 전달할 때, 인수가 가변 객체인 경우, 해당 매개변수를 통해 함수 내부에서 값을 변경할 수 있음.