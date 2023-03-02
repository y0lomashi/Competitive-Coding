from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 1
        i = 1
        chars.append("##")
        while i < len(chars):
            if chars[i] == chars[i - 1]:
                counter += 1
                del chars[i - 1]
                i -= 1
            elif counter > 1:
                for j, char in enumerate(str(counter)):
                    chars.insert(i + j, char)
                counter = 1
                i += j + 1
            i += 1
        return len(chars[:-1])



# ! for testing
chars = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a",]
print(Solution().compress(chars))
