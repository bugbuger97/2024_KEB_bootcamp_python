subjects = {'python':'kim','c++':'sung','datastructure':'kim','database':'kang'}
print("{0[c++]} {0[database]}".format(subjects))

# prime number
number = int(input('Input Number : '))
i = 2
while i < number:
    if number % i == 0:
        print(f'{number} is not prime number')
        break
    i += 1
if i == number:
    print(f'{number} is prime number')