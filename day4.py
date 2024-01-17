# 튜플은 바꿀 수 없다. 그러나 리스트로 바꾼 다음 값을 수정하고 다시 튜플로 바꿔 준다.
# split() : 문자열 -> 리스트로 변경시켜줌.

subjects = ["C++","Java","Python"]
print(subjects[::-1]) # 리스트 반대로 출력함. 그러나 원본은 그대로임.
print(subjects)
subjects.reverse() # 원본이 원래 리스트 반대로 순서가 바뀐다.
print(subjects)

numbers = [1,2,3,4]
print(numbers)
numbers[1:3] = []
print(numbers)