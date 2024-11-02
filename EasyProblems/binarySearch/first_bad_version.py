# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n-1
        while l < r:
            middle =  l+(r-l)//2
            if isBadVersion(middle+1):
                r = middle
            else:
                l = middle+1
        return r+1
