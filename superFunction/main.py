# super() =     Function used to give access to the methods of a parent class.
#               Returns a temporary object of a parent class when used

class Rectangle():
    def __init__(self, length, width):
        self.l = length
        self.w = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length,width)

    def area(self):
        return self.l * self.w

class Cube(Rectangle):

    def __init__(self, l, w, h):
        super().__init__(l,w)
        self.height = h

    def volume(self):
        return self.l * self.w * self.height

squre = Square(3, 3)
cube = Cube(3, 3, 3)

print(squre.area())
print(cube.volume())