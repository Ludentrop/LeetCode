class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums12 = sorted(nums1 + nums2)

        if len(nums12) % 2:
            median = nums12[(len(nums12)-1)//2]
        else:
            median = (nums12[len(nums12)//2] + nums12[len(nums12)//2-1]) / 2

        return median
        
