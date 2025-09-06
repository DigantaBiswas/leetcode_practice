class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pair_map = {}
        operations = 0
        for num in nums:
            if k-num in pair_map and pair_map[k-num] > 0:
                operations += 1
                pair_map[k-num] = pair_map[k-num] - 1
            else:
                if num in pair_map:
                    pair_map[num] = pair_map[num] + 1
                else:
                    pair_map[num] = 1
        return operations 

        
        