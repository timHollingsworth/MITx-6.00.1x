def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    if base <= 0:
        return -1
    if num <= 0:
        return -1
    prev=0
    count=0
    val=base**count
    while val < num:
        prev=count
        count += 1
        val = base**count
    # print(prev,val,count)
    smaller = num - (base**prev)
    larger = (base**count)-num
    # print(smaller,larger)
    if smaller < larger or smaller == larger:
        return prev
    else:
        return count

print(closest_power(10, 550.0))
print(closest_power(7, 196.0))
