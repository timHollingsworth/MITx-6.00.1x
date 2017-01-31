def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    count=0
    vals = []
    for i in listA:
        vals.append((i * listB[count]))
        count += 1
    return sum(vals)
