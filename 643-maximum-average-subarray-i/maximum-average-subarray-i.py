class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        cur_sum = sum(nums[:k])
        max_average = cur_sum/k
        
        while i <len(nums)-k:
            cur_sum += nums[i+k] - nums[i]
            max_average = max(cur_sum/k, max_average)
            i+=1
        return max_average

            