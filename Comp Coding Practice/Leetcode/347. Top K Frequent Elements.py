# Leetcode 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# * first medium problem solved by myself beats 21.25% of python3 submissions

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using dictionary
        num_to_freq = {}
        res = []
        for num in nums:
            if num in num_to_freq:
                num_to_freq[num] += 1
            else:
                num_to_freq[num] = 1
        for i in range(k):
            max_freq = 0
            max_num = None
            for num in num_to_freq:
                if num_to_freq[num] > max_freq:
                    max_freq = num_to_freq[num]
                    max_num = num
            res.append(max_num)
            num_to_freq.pop(max_num)

        return res


# ! for testing
s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([1], 1))

