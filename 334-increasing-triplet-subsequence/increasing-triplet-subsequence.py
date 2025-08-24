class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lowest_number = middle_number = float('inf')

        for num in nums:
            if num<=lowest_number:
                lowest_number = num
            elif num<=middle_number:
                middle_number = num
            else:
                return True
        return False