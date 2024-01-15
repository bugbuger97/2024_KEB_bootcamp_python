# set -> 중복 제거 오름차순 정렬
def Fahrenheit_Celsius(num):
    return (num - 32) * (5/9)
def Celsius_Fahrenheit(num):
    return (num * (9/5)) + 32

if __name__ == '__main__':
    while True:
        menu = input('menu : 1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) Terminated program : ')
        if menu == '3':
            print('Terminated program')
            break
        else:
            if menu == '1':
                num = float(input('Input Fahrenheit : '))
                print(f'{num}F -> {Fahrenheit_Celsius(num):.2f}C')
            elif menu == '2':
                num = float(input('Input Celsius : '))
                print(f'{num}C -> {Celsius_Fahrenheit(num):.2f}F')
            else:
                print('Error')