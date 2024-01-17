sugang = dict(python='kim',db='kang',cpp='sung')
# print(sugang)
# sugang['datastructure'] = 'kim' # add
# print(sugang)
# sugang['datastructure'] = 'park' # update
# print(sugang)
# print(sugang['db'])
# print(sugang.get('db'))
# print(sugang.get('opensource'))
# print(sugang.get('opensource','Not exist'))

for subject,professor in sugang.items():
    print(f'{subject} 과목 담당 교수는 {professor}입니다.') # 버전에 따라서 순서가 섞여서 나올 수도 있다.

for k in sugang.keys():
    print(k)

for v in sugang.values():
    print(v)

for v in sugang.items():
    print(v)
