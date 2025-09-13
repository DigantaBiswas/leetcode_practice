class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flipped = 0
        left_window = 0
        max_count = 0
        for r in range(0, len(nums)):
            if not nums[r]:
                k -= 1
            while k < 0:
                if nums[left_window] == 0:
                    k+=1
                left_window += 1
            max_count = max(max_count, r-left_window+1)

        return max_count


            
