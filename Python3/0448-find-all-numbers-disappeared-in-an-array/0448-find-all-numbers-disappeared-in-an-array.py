class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [-1] * (n+1)
        res = []
        for i in range(n):
            temp[nums[i]] = nums[i]
        
        for i in range(1,n+1):
            if temp[i] == -1:
                res.append(i)
        return res
     
        