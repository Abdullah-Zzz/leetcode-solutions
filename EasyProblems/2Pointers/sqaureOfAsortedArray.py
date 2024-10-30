class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        count = len(nums) -1
        res = [0] * (len(nums))
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                res[count] = nums[j]**2
                j-=1
            else:
                res[count] = nums[i]**2
                i+=1
            count-=1
        return res