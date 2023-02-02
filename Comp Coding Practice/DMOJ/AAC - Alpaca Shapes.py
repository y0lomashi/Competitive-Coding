# Given side length of a square and radius of a circle
# Determine which shape has the larger area
# Print "SQUARE" if square has larger area
# else print "CIRCLE"

s, r = map(int, input().split())
s = s**2
r = (r**2) * 3.14
print("SQUARE" if s > r else "CIRCLE")
