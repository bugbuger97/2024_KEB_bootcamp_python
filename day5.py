# None : 아무 것도 없다는 것을 뜻하는 special value
# None과 False는 완전히 다른 것임.
thing = [None,False,True,'',(),[],0,0.0,set()]

for i in thing:
    if i is None:
        print(f'{i} is nothing')
    elif i:
        print(f'{i} is True')
    else:
        print(f'{i} is False')

'''
None is nothing
False is False
True is True
 is False
() is False
[] is False
0 is False
0.0 is False
set() is False
위 결과 값이 출력된다.
'''