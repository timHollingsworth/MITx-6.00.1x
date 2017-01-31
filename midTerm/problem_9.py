def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    if A == []:
        return A
    if type(A[0]) is list:
        return flatten(A[0]) + flatten(A[1:])
    return A[:1] + flatten(A[1:])
