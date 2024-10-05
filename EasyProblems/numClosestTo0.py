class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        if not nums:
            return []

        #initializing the variable with the first value of the given list "nums", we will keep on updating it with a smaller number as we go through the list. 
        closest = nums[0] 

        # looping through the list
        for i in range(1,len(nums)):
            # abs() gives us the abosolute value. It basically changes a negative number into a positive number.
            # consider this list [-4,2,-5,6], we turn all the number to positive to easily check which one is closer to 0 
            # we check wheather the abs value of number is less than the abs value of the number stored in the closest variable. If it is smaller then we update closest
            # to the smaller number
            if abs(nums[i]) < abs(closest):
                closest = nums[i]

            # the question also said to return the greater number in case there were two numbers close to 0. for example: -1,1
            # one is negative and one is postive but both of them are the same times apart from 0 
            # we the numbers to positive number and then check wheather they are equal if they are we update closest with the greater number
            elif abs(nums[i]) == abs(closest):
                if abs(nums[i]) > closest:
                    closest = nums[i]

        return closest 

