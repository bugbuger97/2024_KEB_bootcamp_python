def Fahrenheit_Celsius(num):
    return (num - 32) * (5/9)
def Celsius_Fahrenheit(num):
    return (num * (9/5)) + 32

def judge_prime(number):
    if number != 1:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
def prime(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    prime_number = list(range(num1 + 1, num2))
    for i in range(num1+1, num2):
        for j in range(2,i):
            if i % j == 0:
                prime_number.remove(i)
                break
    return prime_number

if __name__ == '__main__':
    while True:
        menu = input('menu : 1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) 소수 판정 4) 두 수 사이의 소수 나열 5) Terminated program : ')
        if menu == '1':
            num = float(input('Input Fahrenheit : '))
            print(f'{num}F -> {Fahrenheit_Celsius(num):.2f}C')
        elif menu == '2':
            num = float(input('Input Celsius : '))
            print(f'{num}C -> {Celsius_Fahrenheit(num):.2f}F')
        elif menu == '3':
            number = int(input('Input Number : '))
            if judge_prime(number):
                print(f'{number} is prime number')
            else:
                print(f'{number} is not prime number')
        elif menu == '4':
            num1, num2 = input('Input Num1, Num2 : ').split()
            print(*prime(int(num1), int(num2)))
        elif menu == '5':
            print('Terminated program')
            break
        else:
            print('Error')