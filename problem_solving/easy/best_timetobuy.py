class Solution:
    def maxProfit(self, prices) -> int:
        mx=0
        least=prices[0]
        for i in range(len(prices)-1):
            if least > prices[i+1]:
                least=prices[i+1]
            else:
                if prices[i+1]-least> mx:
                    mx =prices[i+1]-least
        return mx            
                