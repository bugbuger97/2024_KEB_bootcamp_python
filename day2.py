# 화씨 -> 섭씨
def Fahrenheit_Celsius(F):
    return (F-32) * (5/9)
F = float(input('Input Fahrenheit : '))
print('화씨 : %dF, 섭씨 : %0.3fC' %(F,Fahrenheit_Celsius(F)))
print(f'화씨 : {F}F, 섭씨 : {Fahrenheit_Celsius(F):.3f}C') # f-string 소수점 자릿수 설정 -> :.3f이다.