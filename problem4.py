from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=len(nums1) + len(nums2)
        
        if l%2==1:
            return self.rearrange(nums1, nums2, 0, len(nums1)-1, 0, len(nums2)-1, l//2)
        else:
            middle1= self.rearrange(nums1, nums2, 0, len(nums1)-1, 0, len(nums2)-1, l//2)
            middle2= self.rearrange(nums1, nums2, 0, len(nums1)-1, 0, len(nums2)-1, l//2-1)
            return (middle1+middle2)/2

    def rearrange(self, list1, list2, start1, end1, start2, end2, k):
        if start1>end1:
            return list2[k-start1]
        if start2>end2:
            return list1[k-start2]
        
        median1=(start1+end1)//2
        median2=(start2+end2)//2
        median_value1=list1[median1]
        median_value2=list2[median2]

        if (median1+median2)<k:
            if median_value1>median_value2:
                return self.rearrange(list1,list2, start1, end1, median2+1, end2,k)
            else:
                return self.rearrange(list1,list2, median1+1, end1, start2, end2,k)
        else:
            if median_value1>median_value2:
                return self.rearrange(list1,list2, start1, median1-1, start2, end2,k)
            else:
                return self.rearrange(list1,list2, start1, end1, start2, median2-1,k)

    
        

