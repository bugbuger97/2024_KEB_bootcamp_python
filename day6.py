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
    def attack(self):
        print('공격')
    def get_name(self):
        print("inside getter")
        return self.name
    def set_name(self,new_name):
        print("inside setter")
        self.name = new_name
        return
class Charizard(Pokemon,FlyingMixin):
    pass
class Gyarados(Pokemon,SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
# print(g1.swim())
# print(c1.fly())
# c1.attack()
# Charizard.attack(c1) # ()안에 객체가 와줘야 함.
print(g1.name)
g1.name = '잉어킹' # direct access(위험할 수도 있음.)
print(g1.name)

print(g1.get_name())
g1.set_name('잉어')
print(g1.get_name())
