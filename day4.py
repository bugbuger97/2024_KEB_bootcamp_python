# shallow copy
subjects = ["a","b","c"]
a = subjects # shallow copy
b = subjects.copy() # shallow copy
c = list(subjects) # shallow copy
d = subjects[:] # shallow copy
print(subjects,a,b,c,d)
subjects[1] = "x"
print(subjects,a,b,c,d)

import copy
subjects = ["a",["b","c"],"d"]
a = subjects # shallow copy
b = subjects.copy() # shallow copy
c = list(subjects) # shallow copy
d = subjects[:] # shallow copy
e = copy.deepcopy(subjects) # deep copy
print(subjects,a,b,c,d,e)
subjects[1][1]= "x"
print(subjects,a,b,c,d,e) # deep copy인 e만 변하지 않는 것을 볼 수 있다.
