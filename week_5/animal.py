class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newAge):
        self.age = newAge
    def set_name(self, newName=''):
        self.name = newName
    def __str__(self):
        return "Animal:" + str(self.name) + ":" + str(self.age)
class Dog(Animal):
    def speak(self):
        print("bark")
    def __str__(self):
        return "Dog:"+str(self.name)+":"+str(self.age)
class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
        return "Cat:"+str(self.name)+":"+str(self.age)
if __name__ == '__main__':
    myanimal = Animal(1)
    print(myanimal)
    myanimal.set_name('Odin')
    myanimal.set_age(2)
    print(myanimal)
    myDog = Dog(2)
    myDog.set_name("Odin")
    myDog.speak()
    print(myDog)
