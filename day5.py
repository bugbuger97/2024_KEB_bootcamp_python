# def : to reuse the code
# 객체 지향 프로그래밍 원칙 : 단일 체계의 원칙 -> 해당 함수나 해당 클래스는 하나의 원칙에 충실해야 한다.
def is_prime(number) -> bool: # -> bool은 함수의 결과값에 hint를 줌으로서 가독성을 높인다.
    '''
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean 타입으로 리턴
    :param number: 판정할 매개변수
    :return: 소수면 True 소수가 아니면 Flase
    '''
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
    return False

if __name__ == "__main__":
    help(is_prime)
    number = int(input('Input number : '))
    if is_prime(number):
        print(f'{number} is prime number')
    else:
        print(f'{number} is not prime number')