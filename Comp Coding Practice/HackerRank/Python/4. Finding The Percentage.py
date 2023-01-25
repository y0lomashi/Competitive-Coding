
#Inputs Amount of students, students and marks, Which student's average
# ! Uses Dictionary

student_marks = {}
for _ in range(int(input())):
  name, *line = input().split()
  scores = list(map(float, line))
  student_marks[name] = scores
  
query_name = input()
# calculate average by taking the 3 values linked to the key
# format '.2f' sets it to round to 2 decimal places
average = format(((student_marks[query_name][0]+student_marks[query_name][1]+student_marks[query_name][2])/3),'.2f')
print(average)