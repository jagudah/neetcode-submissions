class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l, r = 0, 1

        while r < len(prices):
            currProfit = prices[r] - prices[l]
            if currProfit > result:
                result = currProfit
            r += 1

            if r == len(prices):
                l += 1
                r = l + 1
        return result