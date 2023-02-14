import sys

# * Suffix Tree Method
for _ in range(int(sys.stdin.readline())):
    strLength = len(sys.stdin.readline())
    







# ! TLE AND MLE INEFFICIENT SOLUTION
# for _ in range(int(sys.stdin.readline())):
#     str = sys.stdin.readline()
#     result = set()
#     # List All Substrings
#     for i in range(len(str)+1):
#         for j in range(i, len(str)):
#             # Add each substring in Set
#             result.add(str[i:j])
#     print(len(result))
