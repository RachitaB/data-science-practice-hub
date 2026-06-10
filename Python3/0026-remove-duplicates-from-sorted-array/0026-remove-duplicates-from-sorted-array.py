class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        res = set()
        unique_count = 0
        for i in range(n):
            if nums[i] not in res:
                res.add(nums[i])
                nums[unique_count] = nums[i]
                unique_count += 1
        return unique_count

            
        