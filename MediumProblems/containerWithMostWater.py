#Input: height = [1,8,6,2,5,4,8,3,7]
#Output: 49
#we use a two pointers approach.The height will be the minimum of the value at the index and i and j . The breadth will be the indexes between i and j. The area
#will be equal to length into breadth. we increment i or decrement j based on which one of them is greater because we want the maximun area thus we want a greater
#length .

class Solution:
    def maxArea(self, height: List[int]) -> int:
        out = 0
        i = 0
        j = len(height)-1 
        while i <j:
            breadth = j-i
            length = min(height[i], height[j])
            capacity = breadth*length
            if capacity > out:
                out = capacity
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return out
                
