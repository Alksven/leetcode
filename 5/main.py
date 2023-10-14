class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        b = ['IV', 'IX', "XL", "XC", "CD", "CM"]
        for i in s:
            result += num[i]
        for i_2 in b:
            if i_2 in s:
                result -= num[i_2[0]] * 2
        return result