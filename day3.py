contents = 'How many times does the three-letter sequence the occur?'
word = 'the'
print(contents.count(word))
print(word.isalnum()) # isalnum() : 문자열이 영어, 한글 혹은 숫자로 되어있으면 참 리턴, 아니면 거짓 리턴.
print(contents.isalnum()) # 공백이 있기 때문에 Flase가 됨.

setup = 'a duck goes into a bar....'
print(setup.rstrip('.'))
print(setup.capitalize())
print(setup.center(30))

num = '7.03'
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.0345) # 지수형 부동소수
print('%g' % 7.03) # 일반형: 값에 따라 %e 혹은 %f 사용
print('%d%%' % 100) # %를 출력시키려면 %를 2번 입력함.

strings = '   111woodchck'
print('%-3.8s' % strings)