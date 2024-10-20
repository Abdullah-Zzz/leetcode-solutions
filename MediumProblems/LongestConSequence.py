# we first store the numbers in nums into a hashmap so we have constant lookup time. we go through every num in nums checking if num-1 exists which means that
#it is the start of a seq . If it is then we check for how long the seq is by incrementing num. 


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        out = 0
        for num in nums:
            if num-1 not in hashmap:
                cur_num = num
                current_streak = 1
                while cur_num+1 in hashmap:
                    cur_num +=1
                    current_streak +=1
                out = max(out,current_streak)
        return out