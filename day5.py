# 내부 함수 : 반복문이나 코드 중복을 피하고자 또 다른 함수 내에 어떤 복잡한 작업을 1번 이상 수행할 때, 유용하게 사용됨.
def Two_Input(a,b):
    def Add(c,d):
        return c+d
    return Add(a,b)

print(Two_Input(1,2))

# Closures : 다른 함수에 의해서 동적으로 생성됨.
# def out_func(n_out): # 내부 함수 활용
#     def inner_func(n_in):
#         return n_in * n_in
#     return inner_func(n_out)
# print(out_func(5))

def out_func(n_out): # 클로저 활용
    def inner_func():
        return n_out * n_out
    return inner_func
x = out_func(5)
print(type(x))
print(x)
print(x())

