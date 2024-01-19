class Pokemon:
    def __init__(self,name):
        self.name = name
    def attack(self,target):
        print(f'{self.name}이(가) {target.name}을(를) 공격!')
class Pikachu(Pokemon): # inherit : is-a
    def __init__(self,name,type):
        super().__init__(name) # super() -> 부모의 init 메서드를 호출
        self.type = type
    def attack(self,target): # method override(대체)
        print(f'{self.name}이(가) {target.name}을(를) 백만볼트 공격!')
    def info(self):
        print(f'{self.name}는(은) {self.type} 계열의 포켓몬입니다.')
class Squirtle(Pokemon): # inherit : is-a
    def attack(self,target):
        print(f'{self.name}이(가) {target.name}을(를) 물대포 공격!')
class Augumon:
    pass

p1 = Pikachu("피카츄","전기")
p2 = Squirtle("꼬부기")
p3 = Pokemon("아무무")
print(p1.name) # 자식한테 .name이 없으면, 부모를 찾아간다.
# 추상 클래스(abstract class) : 예시) 도형, 포유류, 운동 선수 그릴 수 없는 거대한 추상적인 개념의 클래스 (분류하기 위해 사용)
print(issubclass(Pikachu,Pokemon))
print(issubclass(Augumon,Pokemon))
p1.attack(p2)
p2.attack(p1)
p1.info()