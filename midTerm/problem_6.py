# def deep_reverse(A):
#     """ assumes L is a list of lists whose elements are ints
#     Mutates L such that it reverses its elements and also
#     reverses the order of the int elements in every element of L.
#     It does not return anything.
#     """
#     # Your code here

def deep_reverse(L):
    for element in L:
        element.reverse()
    L.reverse()
