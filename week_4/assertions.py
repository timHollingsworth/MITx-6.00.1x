"""
use an assert statement to rain an AssertionError
    an example of good defensive programming


"""

def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)

print(avg([]))
