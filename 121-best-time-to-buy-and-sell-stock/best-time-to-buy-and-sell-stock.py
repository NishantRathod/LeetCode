class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        bestBuy = prices[0]
        maxProfit = 0
        for i in range(1,n):
            if prices[i] > bestBuy:
                maxProfit = max(maxProfit ,prices[i] - bestBuy)
            bestBuy = min(bestBuy , prices[i])       
        return maxProfit