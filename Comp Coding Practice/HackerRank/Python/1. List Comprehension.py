
# ! List comprehension
#gets 4 integer inputs for the variables 
a, b, c, n = [int(input("Enter Numbers here: "))for i in range(4)]
#prints list comprehension line
#list x,y,z printed for all combonations of variables a,b,c that dont add to n
print([[x,y,z]for x in range(a+1)for y in range(b+1)for z in range(c+1) if x+y+z!=n])

