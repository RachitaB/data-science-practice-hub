class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_arr = nums1+nums2
        median = 0
        merge_arr.sort()
        mid = (len(merge_arr)-1)//2
        
        if len(merge_arr)%2!=0:
            median = merge_arr[mid]
        else:
            median = (merge_arr[mid] + merge_arr[mid+1])/2
        
        return median

