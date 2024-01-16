# replace()
course = "KEB 2024 KEB Bootcamp"
print(course)
# course = course.replace('KEB','Inha') # replace update
#course = course.replace('KEB','Inha',1)
#print(course)

# strip() : 불필요한 좌우 공백 제거
# lstrip() : 불필요한 왼쪽 공백 제거
# rstrip() : 불필요한 오른쪽 공백 제거
blurt = "What? the...!!?????"
print(blurt)
blurt = blurt.strip('.!?')
print(blurt) # 중간에 들어가 있는 특수기호는 제거하지 못함.

# startswith('내용') : '내용'으로 시작하나? 맞으면 -> True
# endswith('내용') : '내용'으로 끝나나? 맞으면 -> True
# find('내용') : '내용'의 인덱스 번호 반환
# rfind('내용') : 리버스 파인트 -> 오른쪽부터 찾으면서 '내용'의 인덱스 번호 반환
# find에서 -1이 반환 되면 '내용'이 없는 것이다.
print(course.find('KEB'))
print(course.index('2024'))