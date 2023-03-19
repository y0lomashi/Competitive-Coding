# de Polignac's formula
# To find number of trailing zeros in factorial:
# floor(num/5^i) + floor(num/5^i+1)
# until 5^i > num
# * num is the subfactorial (ex. 5! -> 5 is subfactorial)


n = int(input())
i = 1
result = 0
while n >= i:
    i *= 5
    result += n//i
print(result)
