subjects = "python c++ database linux"
if subjects.find('c++') != -1:
    print(f'해당 과목 c++은 존재합니다. 위치는 {subjects.find('c++')}번 인덱스입니다.')
else:
    print(f'해당 과목 c++이 존재하지 않습니다.')