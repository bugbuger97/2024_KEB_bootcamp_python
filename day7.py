# has-a 관계
# aggregation : 전체와 부분의 연관 관계이지만, composition보다 약한 부분의 연관 관계임. ex) 학생-공부
# composition : 전체와 부분의 강력한 연관 관계를 맺는다. ex) 인간-심장 관계
class FlyingMixin:
    def fly(self):
        return f"하늘을 훨훨 날아갑니다~"
class Nofly(FlyingMixin):
    def fly(self):
        return f"하늘을 날 수 없습니다."
class Flywithwings(FlyingMixin):
    def fly(self):
        return f"날개를 통해 하늘을 훨훨 날아갑니다~"

class Jetpack(FlyingMixin):
    def fly(self):
        return f'로켓 추진기로 하늘을 날아갑니다.'

class SwimmingMixin:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name, hp, fly):
        self.__name = name
        self.hp = hp
        self.fly = fly

    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return self.__name + "입니다."
    def __add__(self, other):
        return self.__name + ", " + other.__name + "가 함께 있습니다."

class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

nofly = Nofly()
g1 = Gyarados("갸라도스",120,nofly) # LSP
print(g1.fly.fly())
wings = Flywithwings() # has-a 관계
c1 = Charizard("리자몽",120,wings) # LSP
jet = Jetpack()
g1 = Gyarados("갸라도스",120,jet)
print(c1.fly.fly())
print(g1.fly.fly())
print(g1)
print(c1)
print(g1+c1)
