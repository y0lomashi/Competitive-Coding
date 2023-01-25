
# take n amount of inputs and create a tuple with those integers 
# compute and print result of hash(t)

# input for number of numbers being inputted 
n = int(input())

if n > 0:
  nums = input().split()
  #turns all strings from input into integers and makes it a tuple
  input_list = tuple([int(x) for x in nums])
  #prints the hash of tuple
  print (hash(input_list))
else: 
  exit()