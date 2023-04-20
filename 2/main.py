class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        result = -1
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            if i != 0:
                left += nums[i - 1]
            right -= nums[i]
            if left == right:
                result = i
                break
        return result
