class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = list(str(x))
        b = len(a) % 2
        c = len(a) // 2
        left = a[:c]
        right = a[c:][::-1]
        if b != 0:
            right.pop()
        if left == right:
            return True
        return False
