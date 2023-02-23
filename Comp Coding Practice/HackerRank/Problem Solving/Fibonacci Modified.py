


def fib(t1, t2, n):
    # Write your code here
    dp = []
    dp.append(t1)
    dp.append(t2)
    for i in range(2, n):
        dp.append(dp[i - 1] ** 2 + dp[i - 2])
    return dp[n - 1]


first_multiple_input = input().rstrip().split()

t1 = int(first_multiple_input[0])

t2 = int(first_multiple_input[1])

n = int(first_multiple_input[2])


print(fib(t1, t2, n))
