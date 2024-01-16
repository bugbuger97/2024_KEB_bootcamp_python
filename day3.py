def judge_prime(num1, num2):
    if num1 <= num2:
        prime_number = list(range(num1 + 1, num2))
        for i in range(num1+1, num2):
            for j in range(2,i):
                if i % j == 0:
                    prime_number.remove(i)
                    break
    else:
        prime_number = list(range(num2 + 1, num1))
        for i in range(num2 + 1, num1):
            for j in range(2, i):
                if i % j == 0:
                    prime_number.remove(i)
                    break
    return prime_number

if __name__ == '__main__':
    num1,num2 = input('Input Num1, Num2 : ').split()
    print(*judge_prime(int(num1), int(num2)))