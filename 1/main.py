
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = list()
        summ_add = 0
        for i in nums:
            summ_add += i
            result.append(summ_add)
        return result
