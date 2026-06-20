class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [-1 for i in range(n+1)]
        
        for num in nums:
            temp[num] = num
        
        for i in range(len(temp)):
            if temp[i] == -1:
                return i
        

