import sys


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

if a >= 20 and a <= 23:
    if b >= 6 and b <= 9:
        calc = 24-a + b
        if calc >= 8 and calc <= 10:
            print("Healthy")
        else:
            print("Unhealthy")
    else:
        print("Unhealthy")
else:
    print("Unhealthy")