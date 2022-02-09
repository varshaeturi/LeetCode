class Solution:
    def maxProfit(self, prices):  
        l = 0
        r = l+1 
        diff = 0

        while r <= len(prices)-1:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                diff = max(diff, profit)
                
            else:
                l = r 


            r+=1
       
        return(diff)


print(Solution().maxProfit([7,1,5,3,6,4]))