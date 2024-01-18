# lambda : Anonymous functions

def squares(n):
    return n*n

even_numbers = [i for i in range(11) if i % 2 == 0]

print(even_numbers)
print(tuple(map(squares, even_numbers))) # (0, 4, 16, 36, 64, 100)

# 위의 코드를 lambda를 써서 해결해 보자.
print(tuple(map(lambda x: x*x,even_numbers))) # (0, 4, 16, 36, 64, 100)

z = lambda x:pow(x,2)
print(tuple(map(z,even_numbers))) # (0, 4, 16, 36, 64, 100)