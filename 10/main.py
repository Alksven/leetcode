class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = int("".join(map(str, digits)))
        number += 1
        result = [int(digit) for digit in str(number)]
        return result
