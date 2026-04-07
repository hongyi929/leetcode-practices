class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProf = 0
        minBuy = prices[0]
        for i in range(0, n):
            if i == 0:
                continue
            elif prices[i-1] < minBuy:
                minBuy = prices[i-1]
            possProfit = prices[i] - minBuy
            if possProfit > maxProf:
                maxProf = possProfit
        return maxProf