#Fibonacci recursion
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(1))
print(fib(4))
print(fib(0))
print(fib(11))
