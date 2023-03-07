"""
Liskov Substitution Principle (LSP) is a principle in object-oriented programming
that states that objects of a superclass should be able to be replaced with
objects of its subclasses without affecting the correctness of the program.
In other words, a subclass should be able to be substituted for its superclass
without breaking the code
"""

#  Example 1
class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)


#  Example 2

"""
In this example, the Animal class is the superclass, and Dog and Cat are the subclasses.
They both inherit from the Animal class and override the make_sound method.
The animal_sounds function takes a list of animals, and each animal in the list
is expected to have a make_sound method.

Since Dog and Cat are both subclasses of Animal, they can be substituted for Animal
without breaking the animal_sounds function. This is an example of Liskov Substitution,
as the code is designed to be extensible and flexible to changes in the future.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplementedError

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

dog = Dog("Fido")
cat = Cat("Whiskers")
animal_sounds([dog, cat])
