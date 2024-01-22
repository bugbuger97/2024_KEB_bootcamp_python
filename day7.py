# has-a 관계
# aggregation : 전체와 부분의 연관 관계이지만, composition보다 약한 부분의 연관 관계임. ex) 학생-공부
# composition : 전체와 부분의 강력한 연관 관계를 맺는다. ex) 인간-심장 관계
# 리스코프 치환 원칙 : 서브 타입은 언제나 기반 타입으로 교체할 수 있어야 한다는 것.
# 교체 : 자식 클래스는 최소한 자신의 부모 클래스에서 가능한 행위는 수행이 보장되어야 한다는 의미이다.
# 부모 클래스의 인스턴스를 사용하는 위치에 자식 클래스의 인스턴스를 대신 사용했을 때, 코드가 원래 의도대로 작동해야 한다는 의미이다.
# 부모 클래스와 자식 클래스 사이의 행위가 일관성이 있어야 함.(다형성의 원리를 얘기하는 것임.)
# 다형성 기능을 이용하기 위해서는 클래스를 상속 시켜 타입을 통합할 수 있게 설정해야 함.

class FlyingBehavior:
    def fly(self):
        return f"하늘을 훨훨 날아갑니다~"


class JetPack(FlyingBehavior):
    def fly(self):
        return f"로켓추진기로 하늘을 날아갑니다!"


class NoFly(FlyingBehavior):
    def fly(self):
        return f"하늘을 날 수 없습니다."


class FlyWithWings(FlyingBehavior):
    def fly(self):
        return f"날개로 하늘을 훨훨 날아갑니다"



class Pikachu:
    def __init__(self, name, hp, fly):
        self.name = name
        self.hp = hp
        self.fly_behavior = fly  # aggregation


nofly = NoFly()
p1 = Pikachu("피카츄", 35, nofly)
print(p1.fly_behavior.fly())