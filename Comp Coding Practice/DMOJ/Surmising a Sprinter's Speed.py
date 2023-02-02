# Find max speed of sprinter given n times and distances
# output max speed that the sprinter reached


positions = []
for _ in range(int(input())):
    # take in the position and time and append to positions
    positions.append([int(x) for x in input().split()])

# sort the positions by time
positions.sort(key=lambda x: x[0])

max_diff = 0
for i in range(1, len(positions)):
    distance = abs(positions[i][1] - positions[i - 1][1])
    time = positions[i][0] - positions[i - 1][0]
    diff = distance / time
    if diff > max_diff:
        max_diff = diff

print(max_diff)
