# 2011 CCC S2 Multiple Choice
# https://dmoj.ca/problem/ccc11s2
# Bot to mark multiple choice tests

studentAns, correctAns = [], []

n = int(input())
for _ in range(n):
    sa = input()
    studentAns.append(sa)
for _ in range(n):
    ca = input()
    correctAns.append(ca)

score = 0
for i in range(n):
    if studentAns[i] == correctAns[i]:
        score += 1

print(score)
