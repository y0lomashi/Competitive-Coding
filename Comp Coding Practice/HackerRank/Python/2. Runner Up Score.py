

#n is amount of scores
n = int(input())
#arr is array of n amount of integers
#listify
#map function to apply int to all inputs 
#split to separate by white spaces in list
arr = list(map(int, input().split()))
#sorted in asending order
#set removes duplicates by returning a dictionary that has been converted to a list
arr = sorted(set(arr), reverse = False)
#returns second last value of list, which is second last score
ans = arr[-2]

print(ans)