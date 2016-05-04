#! user/bin/python
def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < 10:
        result.append(b)
        a, b = b, a+b
return result
