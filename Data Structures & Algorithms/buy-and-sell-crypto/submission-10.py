class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r<len(prices):
            res = max(res,prices[r]-prices[l])
            if prices[l] > prices[r]:
                l=r
                r+=1
            else:
                r+=1
        return res