# Fibonacci sequence fucntion
# Video explaining Fibonacci sequence and memoization in python:
# https://www.youtube.com/watch?v=Qk0zUZW-U_M
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input())
print(fib(n))
