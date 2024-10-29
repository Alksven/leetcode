class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        v1 = 1
        v2 = 2

        for i in range(3, n + 1):
            v1, v2 = v2, v1 + v2

        return v2


a = Solution()
b = a.climbStairs(5)
print(b)