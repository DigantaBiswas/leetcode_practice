class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        left_pointer = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[left_pointer] = nums[left_pointer], nums[i]
                left_pointer +=1
            i+=1

        