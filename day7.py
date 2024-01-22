# 인스턴스 메서드 : 메서드 앞에 데코레이터가 업다. 첫번째 인수는 self임.
# 클래스 메서드 : 메서드 앞에 @classmethod 데코레이터가 있다. 첫번째 인수는 cls(예약어인 클래스가 아닌다른 것)임.
# 정적 메서드(static method): @staticmethod 데코레이터가 있다. 첫번째 인수는 위와 같이 자신의 객체나 클래스가 아님.

# static method
class number:
    @staticmethod
    def integer():
        print('int')
number.integer()
# 정적 메서드 : 클래스, 객체에 영향을 미치지 못함.
# 객체를 생성할 필요가 없음.