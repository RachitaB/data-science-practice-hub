class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        n=len(nums)
        for val in nums:
            freq[val] += 1
    
        for key,val in freq.items():
            if val > (n//2):
                return key
        return 0