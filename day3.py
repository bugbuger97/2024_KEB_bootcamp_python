# while - else문 가능 -> while문 안에 break가 실행되지 않으면 else구문이 실행됨.
strings = 'abcdefghijklmnopqrstuvwxyz'
for i in strings:
    print(i)
print('\n') # 2칸 띄우기

univ = 'inha'
i=0
while i < len(univ):
    print(univ[i], end=' ')
    i+=1

print()

for letter in univ:
    print(letter, end=' ')

print()

# for k in range(0,len(univ),1):
# for k in range(0,len(univ)):
for k in range(len(univ)):
    print(univ[k], end=' ')