class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        print(len(prices))
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit+=prices[i+1]-prices[i]
            else:
                continue
        return profit
