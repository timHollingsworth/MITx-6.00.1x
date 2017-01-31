def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) <= 1:
        return char == aStr
    aStr = ''.join(sorted(aStr))
    mid = int((len(aStr)-1)/2)
    if len(aStr) <= 2:
        return True if char == aStr[0] or char == aStr[1] else False
    elif char == aStr[mid]:
        return True
    else:
        if char > aStr[mid]:
            return isIn(char,aStr[mid:])
        else:
            return isIn(char,aStr[0:mid])
print(isIn('j','abjp'))
