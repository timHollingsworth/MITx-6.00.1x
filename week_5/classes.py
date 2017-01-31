class Coordinate(object):
    """
    Coordinate is a subclass of object
    object is the parent class of coordinate

    data attributes:
        think of data as other objects that make up the class
    procedural attributes(methods)
    """

    def __init__(self,x,y):
        """
        Initialize data attributes
        self binds the varaibles to this instance
        """
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.distance(origin))
