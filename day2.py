# Indentation : 파이썬은 들여쓰기 필수
# Precedence : 우선 순위 숙지
# not -> Reverse True == False, Reverse False == True

# temp = [0] # 원소가 존재하는 리스트
# temp = [] # 비어 있는 리스트
# if temp:
#     print("원속가 존재하는 리스트")
# else:
#     print("비어 있는 리스트")

letter = input('Input alphabet letter : ')
# vowels = {'a','e','i','o','u'} # set
vowels = 'aeiou' # str
print(type(vowels))
if letter in vowels: # in
    print(f'{letter} is a vowel')
else:
    print(f'{letter} is a consonant')