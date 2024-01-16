# string split
course = "2024 KEB bootcamp"
print(course)
print(course.split()) # split의 구분자 ' '(스페이스 바)이다.
print(course.split('B')) # split의 구분자 'B'이다.

# numbers = input('FirstNumber SecondNumber : ').split() # type -> list
# print(numbers)
# print(numbers[0] + numbers[1]) # concatenation
# print(int(numbers[0]) + int(numbers[1])) # arithmetic operation

# join() : list -> string
# '원소 사이에 집어 넣을 문자'.join(문자열로 바꿀 리스트)
subjects = ['python','c++','database']
subjects_string = ' / '.join(subjects)
print(subjects_string)