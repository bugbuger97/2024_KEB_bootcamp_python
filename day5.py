import copy
# shallow copy, deep copy 차이 정확히 알기
# Shallow copy : 새로운 복합 객체를 만들고, 원본 객체를 가리키는 참조를 새로운 복합 객체에 삽입함. (포인터)
# Deep copy : 새로운 복합 객체를 만들고, 재귀적으로 원본 객체의 사본을 새로 만든 복합 객체에 삽입함.

# Case1 : mutable 객체안에 mutable 객체가 포함되어 있을 시
# Shallow copy : 복사 대상은 새로운 공간에 할당되지만, 대상안에 있는 요소는 원본과 동일 대상을 참조함.
# Deep copy : 복사 대상 뿐만 아니라 대상안에 있는 요소들도 새로운 공간에 할당됨.
origin = [[1,2], 3]
sc = copy.copy(origin) # shallow copy
dc = copy.deepcopy(origin) # deep copy
print(origin) # [[1, 2], 3]
print(sc) # [[1, 2], 3]
print(dc) # [[1, 2], 3]
origin[0][0] = 0
print(origin) # [[0, 2], 3]
print(sc) # [[0, 2], 3]
print(dc) # [[1, 2], 3]

print('\n')
# Case2 : immutable 객체안에 mutable객체가 포함되어 있을 시
origin = [1,2]
target = (origin, 3)
sc = copy.copy(target) # shallow copy
dc = copy.deepcopy(target) # deep copy
print(target) # ([1, 2], 3)
print(sc) # ([1, 2], 3)
print(dc) # ([1, 2], 3)
origin[0] = 0
print(target) # ([0, 2], 3)
print(sc) # ([0, 2], 3)
print(dc) # ([1, 2], 3)

print('\n')
# Case3 : immutable 객체안에 immutable객체가 포함되어 있을 시
origin = (1,2)
target = (origin, 3)
sc = copy.copy(target) # shallow copy
dc = copy.deepcopy(target) # deep copy
print(sc)
print(dc)
# Shallow copy, Deep copy 모두 동일하게 동작함.

# Case4 : mutable 객체안에 immutable객체가 포함되어 있을 시
origin = (1,2)
target = [origin, 3]
sc = copy.copy(target) # shallow copy
dc = copy.deepcopy(target) # deep copy
# shallow copy, deep copy 모두 origin 튜플을 참조함.


