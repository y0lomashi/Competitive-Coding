# Given a string with n characters
# If string has less than c consonants or v vowels
# print "YES"
# else print "NO"

consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiouy"

n, c, v = map(int, input().split())
string = input()

counterC, counterV = 0, 0

for i in range(n):
    if counterC > c or counterV > v:
        print("NO")
        break
    else:
        if string[i] == "y":
            counterC += 1
            counterV += 1
        elif string[i] in consonants:
            counterC += 1
            counterV = 0
        elif string[i] in vowels:
            counterV += 1
            counterC = 0

if counterC <= c and counterV <= v:
    print("YES")
    


