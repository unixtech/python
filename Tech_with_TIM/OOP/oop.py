def hello():
    print("Hello")

x = 1
y = 'tr'
print(type(hello))


class Dog:
    def __init__(self, name='Tim'):
        self.name = name
        self.x = 'X'
        self.y = 'Y'
        print(name)

    def bark(self):
        print('bark')


d = Dog()
d.bark()
