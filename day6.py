def test(f):
    '''
    데코레이터 함수, 함수 시작하면 start 출력, 함수 끝나면 end 출력
    :param f: function
    :return: closure function
    '''
    def test_in(*args,**kwargs): # 가변 매개변수이기 때문에 값이 오지 않아도 동작을 함.
        print('start')
        #result = f(*args,**kwargs)
        f()
        print('end')
        #return result
    return test_in

def greeting():
    print('안녕하세요~')

t = test(greeting)
t()