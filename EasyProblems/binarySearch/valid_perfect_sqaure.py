class Solution:
    def isPerfectSquare(self, num: int):
        if num == 1:return True
        l = 0
        r = num-1
        while l < r:
            middle = l+(r-l)//2
            if middle*middle == num:
                return True
            elif middle*middle > num:
                r = middle
            else:
                l = middle+1
        return False