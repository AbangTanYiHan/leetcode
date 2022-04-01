from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0
        start = 0
        end = len(height)-1
        while start<end:
            maxArea= max(maxArea, (end-start)*min(height[start],height[end]))
            if height[start]>height[end]:
                end-=1
            else:
                start+=1
        return maxArea


c=Solution()
data= [1,8,6,2,5,4,8,3,7]
ans=c.maxArea(data)
print(ans)