# Hard
# Greedy approach sort all of elements by increasing end time
# Start going back from end time adding times into set
# Subtract from duration of current task.
# Also check if the start of the next task is overlapping
# With the current time we are on
# If so, subtract from the duration of the next task
# * O(n^2) time complexity

from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x : x[1])
        runSet = set()
        for i, e in enumerate(tasks):
            st, end, dur = e
            run = end
            while dur > 0:
                if run not in runSet:
                    runSet.add(run)
                    dur -= 1
                    for j in range(i + 1, len(tasks)):
                        if tasks[j][0] <= run:
                            tasks[j][2] -= 1
                run -= 1
        return len(runSet)
    

# ! for testing
tasks = [[2,3,1],[4,5,1],[1,5,2]]
print(Solution().findMinimumTime(tasks))
