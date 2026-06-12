class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = {}
        for i in nums:
            count = 1
            if i in single_num:
                single_num[i] += 1
            else:
                single_num[i] = count
                
        value = 0
        for k,v in single_num.items():
            if v==1:
                value = k

        return value