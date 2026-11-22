class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = 0
        sell = 1
        while sell != len(prices):
            if prices[sell] > prices[buy]:
                maxP = max(maxP, prices[sell] - prices[buy])
                sell += 1
            else:
                buy = sell
                sell += 1
        return maxP