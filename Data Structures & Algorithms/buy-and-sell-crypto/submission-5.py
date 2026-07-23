class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        maxProfit = 0

        while i < len(prices) - 1:
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)
            j += 1
            
            if j == len(prices):
                i += 1
                j = i + 1
        
        return maxProfit