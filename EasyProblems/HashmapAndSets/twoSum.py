#we make a dict in which we add the previous nums that we have seen with the number as the key and the index as the value. Then we go through the list and 
#check whether the current number minus the target which means the second number that we would add in the current num to make the target is in the dict. 
#for example if the list is nums = [2,7,11,15] and the target is 9 we will go through every num and minus the num from the target : 2-9 = 7 , this gives us the 
#second number that should be added in the current num to make the target. if this num is in the dict we return the indexs of the current number and the number
#in the dict if not we add the number in the dict  


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for index,num in enumerate(nums):
            targ = target - num
            if targ in a:
                return [a[targ],index]
            else:
                a[num] = index
            