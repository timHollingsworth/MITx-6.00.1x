def multi_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(multi_iter(2,2))

#Recursive loop

def mult(a,b):
    if b==1:
        return a
    else:
        return a + mult(a,b-1)
print(mult(3,3))

#Factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(9))

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp <= 0:
        return 1.00
    elif exp == 1:
        return base
    else:
        return base * recurPower(base,exp-1)
