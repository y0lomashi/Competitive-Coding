# Sort an array without using sort function

# * Merge Sort


class Solution:

    def sortArray(self, nums):
        if len(nums) > 1:
            # Get midpoint
            mid = len(nums) // 2
            # Split list in to 2 halves
            l, r = nums[:mid], nums[mid:]

            # Recursively run until length of lists are 1 or less
            self.sortArray(l)
            self.sortArray(r)
            
            # Counter variables
            i = j = k = 0
            while i < len(l) and j < len(r):
                # Check sublists to see which one is smaller
                # Add smaller to list
                if l[i] < r[j]:
                    nums[k] = l[i]
                    i += 1
                else:
                    nums[k] = r[j]
                    j += 1
                k += 1

            # Remaining elements in either left or right will be all greatest
            # So just add them in at the end
            while i < len(l):
                nums[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                nums[k] = r[j]
                j += 1
                k += 1
        return nums

# ! for testing
nums = [1, 2, 4, 1, 2, 3, 4, 9, 1]
print(Solution().mergeSort(nums))
