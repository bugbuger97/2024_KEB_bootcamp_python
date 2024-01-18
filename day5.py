# set : key container -> unorder

alphabet = set('abcdefghhhhh')
print(alphabet) # 중복 없이 무작위 순서로 출력 되어질 수 있음.

# set1.intersection(set2) : 교집합(&)
# set1.union(set2) : 합집합(|)
# set1.difference(set2) : 차집합(-)
# set1.symmetric_difference(set2) : 대칭 차집합(^)

s = set([1,2,3,3,5])
s.add(6)
print(s)

# Create immutable set
fs = frozenset([1,2,3,3,3,5,5])
# fs.add(4) # AttributeError: 'frozenset' object has no attribute 'add'