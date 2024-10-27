#for every position we find the highest height on the left and the right.we find the smaller height between the  left and right height and minus it from the height of the
#current postion. this will give us the the water that can be stored at that position. 


class Solution:
    def trap(self, height):
        leftMax = []
        rightMax = [_ for _ in range(len(height))]
        maxleft = 0
        maxright = 0
        SUM =0
        for i in range(len(height)):
            if i > 0 and height[i-1] > maxleft:
                maxleft = height[i-1]
                leftMax.append(maxleft)
            else:
                leftMax.append(maxleft)
        for i in range(len(height)-1,-1,-1):
            
            if i < len(height)-1 and height[i+1] > maxright:
                maxright = height[i+1]
                rightMax[i] = maxright
            else:
                rightMax[i] = maxright

        for i in range(len(height)):
            potential = min(leftMax[i],rightMax[i])
            if potential-height[i]>0:
                SUM+=potential-height[i]
        return SUM