"""
Your object will be instantiated and called as such:
ty = ToyFactory()
toy = ty.getToy(type)
toy.talk()
"""


class Toy:
    def talk(self):
        raise NotImplementedError('This method should have implemented.')


class Dog(Toy):
    def talk(self):
        print("Wow")


class Cat(Toy):
    def talk(self):
        print("Meow")


class ToyFactory:
    def getToy(self, type):
        if type == "Dog":
            dog = Dog()
            return dog
        elif type == "Cat":
            cat = Cat()
            return cat
        else:
            return None
