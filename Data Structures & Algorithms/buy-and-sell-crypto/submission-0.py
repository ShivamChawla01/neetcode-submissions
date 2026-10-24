class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currProfit = 0
        for i in range(1,len(prices)):
            currProfit += (prices[i] - prices[i-1])
            if(currProfit<0):
                currProfit = 0
            maxProfit = max(currProfit,maxProfit)
        return maxProfit
        