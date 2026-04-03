class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        max_profit = 0
        first = 0
        for i in range(len(prices)):
            profit = prices[i] - prices[first]
            if prices[i] < prices[first]:
                first = i
            max_profit = max(profit,max_profit)
        return max_profit