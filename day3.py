# prime number
def judge_prime(number):
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    if i == number:
        return True

if __name__ == '__main__':
    number = int(input('Input Number : '))
    if judge_prime(number):
        print(f'{number} is prime number')
    else:
        print(f'{number} is not prime number')