class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list(set([val for val in nums1 if val in set(nums2)]))
        return result