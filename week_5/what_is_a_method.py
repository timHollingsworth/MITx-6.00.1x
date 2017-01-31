"""
what is a method?
    function that works only with this class
Python always passes the actual object as the first argument, convention is to use self
as the name
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = y
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**5
    def __str__(self):
        #Print out the class object
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

if __name__ == '__main__':
    c = Coordinate(3,4)
    origin = Coordinate(4,5)
    print("Distance ",c.distance(origin))
    print(c, origin)
    print("Is Instance? " + str(isinstance(c, Coordinate)))
    print(c + origin)
