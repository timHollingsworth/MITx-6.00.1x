def is_even(i):
  """
  Input: i, a positive integer
  Returns True if i is positive
  """
  return i%2==0
def foo(x, y = 5):
    def bar(x):
      return x + 1
    return bar(y * 2)

print(foo(3, 0))
