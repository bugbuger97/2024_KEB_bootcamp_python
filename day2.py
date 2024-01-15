x = 2
y = x + 5  # NameError: name 'x' is not defined
print(y)

print(type(3.14))
print(type(3.14) == float)

'''
isinstance() is one of Python's built-in functions, 
which is used to check whether a given object is an instance of a specified class or one of the classes. 
This function can check whether it is a parent class, a child class, or an instance of the same class.
isinstance(object, classinfo)
'''
print(isinstance(3.14, float))
print(isinstance("Inha", float))
print(isinstance(55, float))

artists = ['BTS', '뉴진스', '핑클', 'SES', 'HOT', '블랙핑크']
groups = artists
print(artists, groups)
artists[2] = '세븐틴'
print(artists, groups)