class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_map = {}
        for i,val in enumerate(nums):
            complement = target - val
            if complement in val_map:
                return [val_map[complement],i]
            val_map[val] = i
        

        