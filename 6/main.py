class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = s
        sym1 = ["(", "{", "["]
        sym2 = [")", "}", "]"]
        sym3 = ["()", "{}", "[]"]
        stop = 1
        for i in range(3):
            if s.count(sym1[i]) != s.count(sym2[i]):
                return False
        while stop != 0:
            stop = 0
            for i in sym3:
                if i in b:
                    b = b.replace(i, "")
                    stop += 1
        if not b:
            return True
        else:
            return False