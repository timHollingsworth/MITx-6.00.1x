#Greatest common divsor
#Iterative and Recursivly
def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    smallest = a if a < b else b
    while True:
        aF = a % smallest==0
        bF = b % smallest==0
        if aF and bF:
            return smallest
        else:
            smallest -= 1
print("Greatest common divisor 4,5 :" + str(gcdIter(4,5)))

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    print(a,b)
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)
print(gcdRecur(256,160))
