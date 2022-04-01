class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        center1=len(nums1)//2
        right=len(nums1)-1
        left=1
        
        for i in range(len(nums2)):
            x=True
            while x==True:
                while nums2[i]<nums1[center1]:
                    right=center1
                    center1=center1//2
                    if right==0 and nums2[i]<nums1[right]:
                        nums1.insert(right,nums2[i])
                        x=False
                        break
                    if right-left==1:
                        nums1.insert(right,nums2[i])
                        x=False
                        break
                while nums2[i]>nums1[center1]:
                    left=center1
                    center1=(center1+right)//2
                    if right==len(nums1)-1 and right-left==1:
                        nums1.insert(right,nums2[i])
                        x=False
                        break   
                    if right==len(nums1)-1 and nums2[i]>nums1[center1]:
                        nums1.insert(right+2,nums2[i])
                        x=False
                        break 
                if x==False:
                    break