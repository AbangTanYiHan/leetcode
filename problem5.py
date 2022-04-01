class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is '': 
            return s
        start=0
        end=0
        for i in range(len(s)):
            len1=self.expandAroundCenter(s,i,i)
            len2=self.expandAroundCenter(s,i,i+1)
            length=max(len1,len2)
            if length>end-start:
                start=i-(length-1)//2
                end= i+length//2
        return s[start:end+1]

    def expandAroundCenter(self,str,a,b)->int:
        while a>=0 and b<len(str) and str[a]==str[b]:
            a-=1
            b+=1
        return b-a-1

