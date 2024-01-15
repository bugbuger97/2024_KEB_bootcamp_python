base_number = int(input('Input base number : '))
exponent_number = int(input('Input exponent number : '))

# f-string
print(f'밑은 {base_number}, 지수는{exponent_number}, 결과 값은 {pow(base_number, exponent_number)}')

# format function -> {}안에 0,1,2를 넣어서 출력할 변수의 순서를 정할 수 있다.
print('밑은 {}, 지수는{}, 결과 값은 {}'.format(base_number,exponent_number,pow(base_number, exponent_number)))
print('밑은 {0}, 지수는{1}, 결과 값은 {2}'.format(base_number,exponent_number,pow(base_number, exponent_number)))

# like C
print('밑은 %d, 지수는 %d, 결과 값은 %d' %(base_number, exponent_number, pow(base_number, exponent_number)))