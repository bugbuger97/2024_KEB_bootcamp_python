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