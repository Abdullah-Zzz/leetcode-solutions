#Example 1: Input: intervals = [[1,3],[2,6],[8,10],[15,18]]  first we will sort out the intervals in ascending order according to the first element in every
#interval. we will look for an overlapping interval by checking whether the first element of the current interval is less than the second element of the previous
#interval . if this is the case the interval is overlapping so we will update the second element of the prevous interval to the greater interval. for example:
# in [1,3] [2,6] we will update the second element of the first interval to 6 so it becomes [1,6].


class Solution:
    def merge(self, intervals: List[List[int]]) ->[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for i in range(1,len(intervals)):
            if output[-1][1] >= intervals[i][0]:
                greaterRange = max(output[-1][1],intervals[i][1])
                output[-1][1] = greaterRange
            else:
                output.append(intervals[i])

        return output