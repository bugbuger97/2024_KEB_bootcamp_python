# 다중 상속 -> 파이썬에서는 클래스 괄호 안에 상속 받은(표기된) 순서대로 부모의 우선순위가 결정된다.
class FlyingMixin:
    def fly(self):
        return f'{self.name} fly~'
class SwimmingMixin:
    def swim(self):
        return f'{self.name} swim~'
class Pokemon:
    def __init__(self,name):
        self.name = name
class Charizard(Pokemon,FlyingMixin):
    pass
class Gyarados(Pokemon,SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
print(g1.swim())
print(c1.fly())