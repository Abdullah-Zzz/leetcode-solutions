#we create a hashmap. we add each unique element as the key and the number of times it is repeated as the value of the key eg: [2,2,1,2], {2:3.1:1} 
#then we just simply check which element in the hashmap has the highest value. since the values are the number of times the key is repeated in the array 
#we can just return the key with the highest value.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        out=0
        times = 0
        for num in nums:
            if num in hashmap:
                hashmap[num] +=1
            else:
                hashmap[num] = 1
        for key in hashmap:
            if hashmap[key] > times:
                times = hashmap[key]
                out = key

        return out