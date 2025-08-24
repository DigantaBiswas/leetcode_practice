class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        ans = [1] * len_nums
        multiplier = 1
        for i in range(0, len_nums):
            ans[i] = multiplier
            multiplier = multiplier * nums[i]
        
        multiplier = 1
        for i in range(len_nums-1, -1, -1):
            ans[i] *= multiplier
            multiplier = nums[i] * multiplier
        return ans


        