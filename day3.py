# 6.1
result = [i for i in range(3,-1,-1)]
print(result)

# 6.2
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
    else:
        print('oops')
        break
    number += 1

# 6.3
guess_me = 5
for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
    else:
        print('oops')
