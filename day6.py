# Async Functions(비동기 함수) : 함수를 정의하는 def 앞에 async 키워드가 붙으면 비동기 함수임.
# 함수를 호출하기 전에 await 키워드가 있으면 해당 함수는 비동기적임.
# 비동기 함수는 실행을 완료하기보다 '제어를 넘겨주는 것'임.

# 예외 처리
import random

numbers = [random.randint(1,100) for i in range(5)]
print(numbers)
try:
    pick = int(input(f'Input index(0 ~ {len(numbers)-1}) : '))
    print(numbers[pick])
    print(10/0)
except IndexError as err:
    print(f'인덱스 범위를 벗어났습니다.\n{err}') # err -> 시스템이 던져준 메시지임.
except ValueError as err:
    print(f'정수만을 입력해주세요.\n{err}')
except Exception as err: # except Exception -> 이 부분은 보험으로 항상 맨 밑에 들어가야 한다.
    print(f'Error occurs!\n{err}')