# def applyF_filterG(A, f, g):
#     """
#     Assumes L is a list of integers
#     Assume functions f and g are defined for you.
#     f takes in an integer, applies a function, returns another integer
#     g takes in an integer, applies a Boolean function,
#         returns either True or False
#     Mutates L such that, for each element i originally in L, L contains
#         i if g(f(i)) returns True, and no other elements
#     Returns the largest element in the mutated L or -1 if the list is empty
#     """
#     # Your code here
#     global L
#     L = list()
#     for i in A:
#         if g(f(i)):
#             L.append(i)
#     return(max(L))
# def f(i):
#     return i + 2
# def g(i):
#     return i > 5
# L = [0, -10, 5, 6, -4]
# print(applyF_filterG(L, f, g))
# print(L)
def f(i):
    return i + 2

def g(i):
    return i > 5

l = [0, -10, 5, 6, -4]
def applyF_filterG(L, f, g):
    for val in L[:]:
        if not g(f(val)):
            L.remove(val)
    return -1 if not L else max(L)

print(l) # [0, -10, 5, 6, -4]
applyF_filterG(l, f, g) # Return 6
print(l) # [5, 6]
