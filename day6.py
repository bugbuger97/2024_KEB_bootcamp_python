import random
class OopsException(Exception):
    pass

numbers = [random.randint(1,100) for i in range(5)]
print(numbers)
try:
    pick = int(input(f'Input index(0 ~ {len(numbers)-1}) : '))
    print(numbers[pick])
    raise OopsException("Oops") # exception!
except IndexError as err:
    print(f'인덱스 범위를 벗어났습니다.\n{err}')
except ValueError as err:
    print(f'정수만을 입력해주세요.\n{err}')
except OopsException as err:
    print(f'Oops Oops {err}')
except Exception as err:
    print(f'Error occurs!\n{err}')
else:
    print(f'Program terminate')