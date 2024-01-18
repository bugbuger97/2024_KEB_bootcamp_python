# dict comprehensions
# 딕셔너리에서 immutable한 것들만 키값이 될수 있다.

# univ = 'inha university'
# counts_alphabet = {letter: univ.count(letter) for letter in univ}
# print(counts_alphabet)

# univ = 'inha university'
# counts_alphabet=dict()
# for letter in univ:
#     counts_alphabet[letter] = univ.count(letter)
# print(counts_alphabet)

# 8.10
squares = {n : n*n for n in range(10)}
print(squares)