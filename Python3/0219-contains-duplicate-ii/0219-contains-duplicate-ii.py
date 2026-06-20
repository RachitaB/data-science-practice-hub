class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = set()
        for i in range(len(nums)):
            if nums[i] in freq:
                return True
            freq.add(nums[i])

            if len(freq) > k:
                freq.remove(nums[i-k])
        return False   