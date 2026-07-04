class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        buyIndex, sellIndex = 0, 1
        maxProfit = 0

        while sellIndex < len(prices):
            currProfit = prices[sellIndex] - prices[buyIndex]

            if currProfit > maxProfit:
                maxProfit = currProfit
                
            if sellIndex == len(prices) - 1:
                buyIndex += 1
                sellIndex = buyIndex + 1
            else:
                sellIndex += 1
        return maxProfit