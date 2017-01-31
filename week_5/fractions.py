class fraction(object):

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
    def __str__(self):
        return str(self.num) + '/' + str(self.denom)

    #Methods
    def getNum(self):
        return self.num
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        numerNew = other.getDenom() * self.getNum() + other.getNum() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNum() - other.getNum() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def convert(self):
        return self.getNum() / self.getDenom()

#Check if running from command line
if __name__ == '__main__':
    one_half = fraction(1,2)
    two_thirds = fraction(2,3)
    print(one_half)
    print(two_thirds)
    # print(one_half.getNum())
    print(one_half + two_thirds)
    print(one_half - two_thirds)
    print(one_half.convert())
