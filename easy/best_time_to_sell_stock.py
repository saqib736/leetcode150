class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_p = 0
        curr_p = 0
        j = 0    
        for i in range(1, len(prices)):
            if prices[i] < prices[j]:
                j = i
            
            curr_p = prices[i] - prices[j]
            if curr_p > max_p:
                max_p = curr_p
                
        return max_p
                
                                       
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    obj = Solution()
    profit = obj.maxProfit(prices)
    print(profit)
    
                

        