#we add the letters of jewels in a dict and check how many letters that are in stones are jewels


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsDict = {}
        output = 0
        for i in jewels:
            jewelsDict[i] = i
        
        for stone in stones:
            if stone in jewelsDict:
                output +=1
            
        return output
