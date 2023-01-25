# create list
# ! nested lists
grades = []
# loop through based on number inputted first
for _ in range(int(input())):
    name = input()
    score = float(input())
    # append name and score into list as nested list
    grades.append([name, score])

# sort grades by score
sorted_grades = sorted(grades, key=lambda x: x[1])
# trim out all people with scores at first place
trim_one = [x for x in sorted_grades if x[1] != sorted_grades[0][1]]
# trim out all people with scores not at second place
final = [y for y in trim_one if y[1] == trim_one[0][1]]
# sort by alphabetical order
final.sort(key=lambda x: x[0])
# iterates through final for each item in final
for i in range(len(final)):
    # prints the first value in the nested lists
    print(final[i][0])
'''
#! Other solution

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])
# takes second highest mark by ordering by marks and removing duplicates and taking the second value
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# * creates newline, only puts a which represents the name into the list
# * a,b = first value, second value = name, mark
# * alphabetically sorted marksheet, looks at each pair a,b and checks if b is equal to second_highest; if so appends it to list
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

'''
