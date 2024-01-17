# Assignment (add prime series program)
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    while True:
        menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime1   4) Prime2   5) Quit program : ")
        if menu == '1':
            fahrenheit = float(input('Input Fahrenheit : '))
            print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
        elif menu == '2':
            celsius = float(input('Input Celsius : '))
            print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
        elif menu == '3':
            number = int(input("Input number : "))
            if number < 2:
                print(f'{number} is NOT prime number!')
            else:
                if is_prime(number):
                    print(f'{number} is prime number')
                else:
                    print(f'{number} is NOT prime number!')
        elif menu == '4':
            numbers = input("Input first second number : ").split()
            n1 = int(numbers[0])
            n2 = int(numbers[1])
            if n1 > n2:
                n1, n2 = n2, n1
            for number in range(n1, n2 + 1):
                if number < 2:
                    continue # pass
                else:
                    if is_prime(number): print(number, end=' ')
            print()
        elif menu == '5':
            print('Terminate Program.')
            break
        else:
            print('Invalid Menu!')