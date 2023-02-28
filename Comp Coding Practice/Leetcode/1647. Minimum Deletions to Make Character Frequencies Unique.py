# Greedy solution count frequency of characters using hashmap
# Subtract frequencies until they are 0 or not in set
# Add values to set once finished


class Solution:
    def minDeletions(self, s: str) -> int:
        map = {}
        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1
        count = 0
        unique = set()
        for char, freq in map.items():
            while freq > 0 and freq in unique:
                count += 1
                freq -= 1
            unique.add(freq)

        return count
