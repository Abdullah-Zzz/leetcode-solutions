#we move through nums and add every num in a dict but bofore adding every num we check whether the num already exists in the dict 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = num
        
        return False