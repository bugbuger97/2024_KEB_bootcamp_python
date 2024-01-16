def judge_prime(number):
    if number != 1:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True


if __name__ == '__main__':
    number = int(input('Input Number : '))
    if judge_prime(number):
        print(f'{number} is prime number')
    else:
        print(f'{number} is not prime number')