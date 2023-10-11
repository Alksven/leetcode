class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = list()
        for i_1 in range(len(nums)):
            for i_2 in range(i_1 + 1, len(nums)):
                if nums[i_1] + nums[i_2] == target:
                    result.append(i_1)
                    result.append(i_2)
                    return result
