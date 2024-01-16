subjects = "python c++ database linux"
subject = input('Input Subject : ')
try:
    print(f'해당 과목 {subject}은 존재합니다. 위치는 {subjects.index(subject)}번 인덱스입니다.')
except ValueError:
    print(f'해당 과목 {subject}이 존재하지 않습니다.')