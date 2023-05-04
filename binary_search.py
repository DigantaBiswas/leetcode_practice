class Solution:
    def search(self, nums, target):
        low = 0
        top = len(nums) - 1

        # while top != 0:
        #     mid = low + top // 2
        #     if nums[mid] > target:
        #         top = mid
        #     elif nums[mid] < target:
        #         low = mid
        #     else:
        #         return mid
        while low <= top:
            mid = low + top // 2
            if nums[mid] > target:
                top = mid
            elif nums[mid] < target:
                low = mid
            else:
                return mid
        return -1


print(Solution().search(nums=[1, 2, 3, 4, 9, 11], target=9))
