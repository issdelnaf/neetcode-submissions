class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        bp=prices[0]
        for i in range(1,n):
            if prices[i]<bp:
                bp=prices[i]
            else:
                profit=max(profit,prices[i]-bp)
        return profit