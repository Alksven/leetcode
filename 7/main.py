class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        word = strs[0]
        if len(word) == 0:
            return ""
        result = ''
        try:
            for i, l in enumerate(word):
                for i_2 in range(1, len(strs)):
                    if strs[i_2][i] != l:
                        return result
                result += l
        except IndexError:
            return result

        return result