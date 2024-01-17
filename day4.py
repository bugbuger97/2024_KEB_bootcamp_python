# Tuple
t1 = (5)
t2 = 5,
t3 = (5,)
t4 = (5,7)
t5 = 5,7
print(type(t1),type(t2),type(t3),type(t4),type(t5))
t6 = "python", "kim" # 이것을 packing이라고 함.
print(type(t6), t6[1])

subject, prof = t6 # unpacking -> unpacking할 때, 정확히 개수가 맞아야 한다.
print(prof) # kim
print(subject) # python

t7 = ()
t8 = tuple()
print(type(t7),type(t8))

t9 = ('abc')
print(type(t9)) # str

print(type(9,), type(((9,)))) # int, tuple

# tuple간의 비교 연산이 가능함.
# '+' 연산으로 튜플간의 합치기 가능함.
t10 = 4.43,
t11 = 3.97, 4.1, 3.27
print(t10+t11) # (4.43, 3.97, 4.1, 3.27)
print(t11+t10) # (3.97, 4.1, 3.27, 4.43)