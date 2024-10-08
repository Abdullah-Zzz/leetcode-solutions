# As we move through the list we will check for two things, wheather the current price is less than the previous least price  
#if it is we will update the buy price to the new least value and if it is not less than the previous least price then we will check wheather the profit 
#that we are making if we sell it with the current price is greater than any other profits we made before

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit