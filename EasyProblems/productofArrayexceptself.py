#first we will find the product of all the nums coming before every number in the list for example 
#in the list [1,2,3,4] for every number we will find the product of all the preceding numbers output:[1,1,2,6]
#then we will find the product of all the number coming after every number for example 
#in the list [1,2,3,4] for every number we will find the product of all the numbers coming after each number output:[24,12,4,1]
# then we will find the product of both of the lists , the preceding one and the exceding one.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [_ for _ in range(len(nums))]
        pre = 1
        for i in range(len(nums)):
            out[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= post
            post *=nums[i]
        
        return out