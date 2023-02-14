import sys
from math import sqrt

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    high, low = num, num
    flagHigh, flagLow = False, False
    while True:
        # important to use sqrt here to reduce time complexity
        # this only loops until the square root of the number
        # this is because any number greater than the square root + 1
        # will not be a factor of the number
        for i in range(2, int(sqrt(high))+ 1):
            if high % i == 0:
                # not prime
                flagHigh = True
                break
        for j in range(2, int(sqrt(low))+ 1):
            if low % j == 0:
                # not prime
                flagLow = True
                break
        if not flagHigh and not flagLow:
            print(low, high)
            break
        else:
            high += 1
            low -= 1
            flagHigh, flagLow = False, False
