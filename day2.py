a = 100
a -= 3 # side effect : 메모리 값의 변화
print(a)

# first_number = int(input("First number : "))
# second_number = int(input("Second number : "))
#
# quotient = first_number // second_number
# remainder = first_number % second_number
# print(f'몫은 {quotient}, 나머지는 {remainder}입니다.')

def divmod(first_number, second_number):
    quotient = first_number // second_number
    remainder = first_number % second_number
    return (quotient, remainder)

if __name__ == '__main__':
    first_number = int(input("First number : "))
    second_number = int(input("Second number : "))
    print(f'몫은 {divmod(first_number, second_number)[0]}, 나머지는 {divmod(first_number, second_number)[1]}입니다.')