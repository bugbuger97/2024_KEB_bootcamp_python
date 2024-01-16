# strings in Python are immutable
# r'contents' : 특수 기호 등 날 것 그대로의 형태를 출력함
university = r"Inha\nuniversity!" # raw string
#print(university)

# num1 = input("First number : ")
# num2 = input("Second number : ")
# print(num1 + num2) # concatenation
# print(num1 * 3) # duplicate
# print(num1 + 3) # error

# string slicing
print(university[:4])
print(university[:-13])
print(university[3::-1])
print(university[6:16])
print(university[11:-4])
print(university[-2:-1])