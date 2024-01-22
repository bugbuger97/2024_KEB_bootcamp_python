# 10.1
class Thing:
    def __init__(self,name="None"):
        self.name = name
    def __str__(self):
        return self.name
example1 = Thing()
example2 = Thing()
print(example1)
print(example2)

# 10.2
class Thing2:
    def __init__(self,letters):
        self.letters = letters
    def __str__(self):
        return self.letters
ex = Thing2('abc')
print(ex)

# 10.4
class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return f'{self.name}, {self.symbol}, {self.number}'
    def dump(self):
        return (self.name,self.symbol,self.number)

element = Element('Hydrogen','H',1)
print(element.name)
print(element.symbol)
print(element.number)

# 10.5
el_dict = dict(name='Hydrogen',symbol='H',number=1)
ex_element = Element(list(el_dict.values())[0],list(el_dict.values())[1],list(el_dict.values())[2])

# 10.6
ex2_element = Element('Hydrogen','H',1)
print(ex2_element.dump())

# 10.7
ex3_element = Element('Hydrogen','H',1)
print(ex3_element)

# 10.8
class Element:
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return f'{self.__name}'
    @name.setter
    def name(self,name):
        self.__name = name

