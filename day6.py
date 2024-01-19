class Pokemon: # 클래스의  앞 글자는 대문자로 시작함.
    def __init__(self, name):
        print(f'{name} 포켓몬스터 생성')

pikachu = Pokemon('피카츄') # 해당 객체당 init이 딱 한번 발생함.
squirtle = Pokemon('꼬부기')
print(pikachu)  # <__main__.Pokemon object at 0x000002C9BDBBD4C0> -> 메모리 번지가 출력됨.
print(squirtle)