class Pokemon:
    pass

pikachu = Pokemon()
squirtle = Pokemon()
pikachu.name = "피카츄"
pikachu.nemesis = squirtle
print(pikachu.name)
pikachu.nemesis.name = "꼬부기"  # squirtle.name = "꼬부기"
print(pikachu.nemesis.name)