# Google Foobar Challenge Lvl 1
# * Solar Doomsday Problem
import math
# create area variable
area = 0
# create empty list
final = []


def solution(area):
    all_areas = [x**2 for x in range(1, int(math.sqrt(1000000) + 1))]
    all_areas.reverse()
    while area > 0:
        for i in range(len(all_areas)):
            if all_areas[i] <= area:
                final.append(all_areas[i])
                area -= all_areas[i]
    print(final)
    return final


solution(41241)
