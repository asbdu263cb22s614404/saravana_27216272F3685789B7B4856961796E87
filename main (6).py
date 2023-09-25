# A Sample class with init method
class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello sir, My friend name is:', self.name)

p1 = Person('RK')
p2 = Person('Manoj')
p3 = Person('Anbuparamesh')
p4 = Person('jawid')
p5 = Person('thirumoorthi')
p6 = Person('sabareesh')
p7 = Person('thamotharan')
p1.say_hi()
p2.say_hi()
p3.say_hi()
p4.say_hi()
p5.say_hi()
p6.say_hi()
p7.say_hi()