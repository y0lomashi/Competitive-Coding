import sys


# -1 because the first person doesn't pass the ball
n = int(sys.stdin.readline()) - 1

# n*(n-1)*(n-2) is the number of passes that the last person doesn't receive
print(int((n*(n-1)*(n-2))/6))
