print(int('1A',16)) # 16진수 -> 26

# 화씨 -> 섭씨
# 섭씨 -> 화씨
def Fahrenheit_Celsius(t):
    if t[-1] == 'F':
        num = float(t[:-1])
        return (num-32) * (5/9)
    else:
        num = float(t[:-1])
        return (num*1.8) + 32

if __name__ == '__main__':
    F = input('Input Fahrenheit : ')
    C = input('Input Celsius : ')
    print(f'화씨 : {F}, 섭씨 : {Fahrenheit_Celsius(F):.2f}C')
    print(f'섭씨 : {C}, 화씨 : {Fahrenheit_Celsius(C):.2f}F')