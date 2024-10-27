#https://www.youtube.com/watch?v=_ZEvmycwXHs

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0]*len(temp)
        stack=[]
        for i,t in enumerate(temp):
            while stack and temp[stack[-1]] < t:
                days = i-stack[-1]
                res[stack[-1]] = days
                stack.pop()
            stack.append(i)
        return res