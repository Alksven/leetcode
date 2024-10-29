class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        min_num = float("inf")

        for i in prices:
            min_num = min(min_num, i)
            ans = max(ans, i - min_num)
        return ans