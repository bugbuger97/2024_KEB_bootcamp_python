# day 2 assignment
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

# day 3 assignment
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

# day 4 assignment
# 8.1
e2f = dict(dog='chien',cat='chat',walrus='morse')
print(e2f)

# 8.2
print(e2f['walrus'])

# 8.3
f2e = {v:k for k,v in e2f.items()}
print(f2e)

# 8.4
print(f2e.get('chien'))

# 8.5
print(e2f.keys())

# 8.6
life = dict(animals=dict(cats='Henri',octopi='Grumpy',emus='Lucy'),plants=dict(),other=dict())
print(life)

# 8.7
print(life.keys())

# 8.8
print(life['animals'].keys())

# 8.9
print(life['animals']['cats'])

# 8.10
squares = {i: i**2 for i in range(10)}
print(squares)

# day 5 assignment
# 9.1
def good(*args):
    List=list(args)
    print(List)
    return List
good('Harry','Ron','Hermione')

# 9.2
def gets_odds():
    odds = [i for i in range(10) if i%2==1]
    for i in odds:
        yield i
something = gets_odds()
print(something)
cnt=0
for i in something:
    cnt+=1
    if cnt == 3:
        print(f'세번째 홀수 : {i}')

# 9.3
def test(f):
    def inner(*args):
        print('Start')
        print(f(*args))
        print('end')
    return inner
@test
def my_int_print(a):
    return a
my_int_print(1)

# day 6 assignment
import pygame
import random
import time
import datetime
'''
<Game Rule>
포켓볼이 무작위로 내려오는데, 피카츄가 그것을 피하면서 가장 오래 살아남기 게임!
1초당 1점이며 점수는 RUN interface에 나옵니다. 
(참고) 이미지는 저작권에 걸릴 수 있기 때문에 올리지 않았습니다.
'''
class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    def Insert_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
        self.size_x, self.size_y = self.img.get_size()
    def Change_size(self, size_x, size_y):
        self.img = pygame.transform.scale(self.img, (size_x, size_y))
        self.size_x, self.size_y = self.img.get_size()
    def Show(self):
        screen.blit(self.img, (self.x, self.y))

def crash(a, b) -> bool:
    '''
    a과 b가 서로 충돌하면 True
    :param a: object a
    :param b: object b
    :return: If a crushes b,Return True
    '''
    if (a.x-b.size_x <= b.x) and (b.x <= a.x+a.size_x):
        if (a.y-b.size_y <= b.y) and (b.y <= a.y+a.size_y):
            return True
        else:
            return False
    else :
        return False

if __name__ == "__main__":
    pygame.init()
    size = [600, 800]
    screen = pygame.display.set_mode(size)
    title = "My Pokemon Game"
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()

    pikachu = obj()
    pikachu.Insert_img("C:/2024_KEB_bootcamp_python/pythonProject/pikachu.png")
    pikachu.Change_size(60, 80)
    pikachu.x = round(size[0] / 2 - pikachu.size_x / 2)
    pikachu.y = size[1] - pikachu.size_y - 15
    pikachu.move = 8

    left_go = False
    right_go = False
    space_go = False
    poketball_list = []
    k = 0
    start = time.time()
    SB = 0
    while SB == 0:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SB = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_go = True
                elif event.key == pygame.K_RIGHT:
                    right_go = True
                    k = 0
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_go = False
                elif event.key == pygame.K_RIGHT:
                    right_go = False

        if left_go == True:
            pikachu.x -= pikachu.move
            if pikachu.x <= 0:
                pikachu.x = 0
        elif right_go == True:
            pikachu.x += pikachu.move
            if pikachu.x >= size[0] - pikachu.size_x:
                pikachu.x = size[0] - pikachu.size_x
        k += 1

        if random.random() > 0.97:
            poketball = obj()
            poketball.Insert_img("C:/2024_KEB_bootcamp_python/pythonProject/poketball.png")
            poketball.Change_size(30, 30)
            poketball.x = random.randrange(0, size[0] - poketball.size_x - round(pikachu.size_x / 2))
            poketball.y = 10
            poketball.move = 6
            poketball_list.append(poketball)
        d_list = []

        for i in range(len(poketball_list)):
            temp = poketball_list[i]
            temp.y += temp.move
            if temp.y >= size[1]:
                d_list.append(i)
        d_list.reverse()
        for d in d_list:
            del poketball_list[d]
        # 포켓볼에 닿으면 게임 종료
        for i in range(len(poketball_list)):
            temp = poketball_list[i]
            if crash(temp, pikachu) == True:
                SB = 1
                time.sleep(1)

        screen.fill((20,130,190))
        pikachu.Show()
        for a in poketball_list:
            a.Show()
        pygame.display.flip()
    pygame.quit()
    end = time.time()
    score = end - start
    print(f'Your score is {round(score)} !!!')