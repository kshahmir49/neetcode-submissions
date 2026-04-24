class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        mprofit = 0
        while p2 < len(prices):
            profit = prices[p2] - prices[p1]
            mprofit = max(mprofit, profit)
            if prices[p2] < prices[p1]: p1 = p2
            p2+=1
        return mprofit