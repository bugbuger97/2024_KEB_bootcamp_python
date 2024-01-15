# divmod -> 파이썬의 내장 함수로서, divmod(나눌 대상, 나눌 값)으로 return (quotient, remainder)이다.
print(divmod(10,2))
print(f'몫은 {divmod(10,2)[0]}\n나머지는 {divmod(10,2)[1]}')

dec = 65 # 10진수
octal = 0o101 # 8진수
hexadecimal = 0x41 # 16진수
binary = 0b01000001 # 2진수
print(dec,octal,hexadecimal,binary)
print(chr(binary)) # chr(number) : 숫자 -> 문자
print(ord('A')) # ord(number) : 문자 -> 숫자