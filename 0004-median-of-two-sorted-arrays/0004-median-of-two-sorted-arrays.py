class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #    l=len(nums2) 
    #    for i in range(0,l):
    #        nums1.append(nums2[i])

        nums3 = nums1 + nums2
        nums3.sort()
        l2=len(nums3)
        if l2 % 2 != 0:
            median=nums3[l2//2]
        else:
            median = ((nums3[l2//2-1]) + ( nums3[l2//2]))/2
        return median     