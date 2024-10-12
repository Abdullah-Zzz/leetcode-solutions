#we make to pointers one to keep track of the starting index of a range and one to keep track of the 
#next element as we move thorugh the list.whenever a range ends we update the start index to the new
#value. if the number is alone and has no range , in such a case the start index will be equal to the
#index of the current num . we can add the number to our result and increment start index by 1. 

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        startIndex = 0 
        j = 1
        for i in range(len(nums)):
            if j < len(nums) and nums[i]+1 == nums[j]:
                pass 
            elif startIndex == i:
                res.append(str(nums[i])) 
                startIndex +=1
            else:
                res.append(f"{nums[startIndex]}->{nums[i]}")
                startIndex = i+1
            j+=1
        return res
