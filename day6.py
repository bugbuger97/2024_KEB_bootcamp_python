class Pokemon:
    def __init__(self, name):
        self.name = name
        print(f'{name} 포켓몬스터 생성')
    def attack(self,target):
        print(f'{self.name}이(가) {target.name}을(를) 공격!')

pikachu = Pokemon('피카츄')
charizard = Pokemon('리자몽')
squirtle = Pokemon('꼬부기')
charizard.attack(squirtle)
# is - a 관계 : 상속 관계 (결합도가 가장 강함.) -> 부모가 가진걸 그대로 가져다 쓸 수 있음.
# has - a 관계
# use - a 관계 : dependency