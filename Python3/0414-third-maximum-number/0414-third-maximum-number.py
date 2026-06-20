class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        temp1 = set(nums)
        n = len(temp1)
        if n<3:
            return max(temp1)
        else:
            temp1.remove(max(temp1))
            temp1.remove(max(temp1))
            return max(temp1)