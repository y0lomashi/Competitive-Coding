from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums = {}
        for i in range(len(nums1)):
            if nums1[i][0] not in nums:
                nums[nums1[i][0]] = nums1[i][1]
            else:
                nums[nums1[i][0]] += nums1[i][1]
        for j in range(len(nums2)):
            if nums2[j][0] not in nums:
                nums[nums2[j][0]] = nums2[j][1]
            else:
                nums[nums2[j][0]] += nums2[j][1]
        nums = sorted(nums.items(), key=lambda x: x[0])

        return nums


# ! for testing

nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]
print(Solution().mergeArrays(nums1, nums2))
        
