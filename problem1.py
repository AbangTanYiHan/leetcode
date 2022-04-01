from pickle import FALSE
import re

class Solution:
    
    def isMatch(s: str, p: str) -> bool: 
        res = ""

        for i in range(len(p)):
            if p[i] == ".":
                res += "[a-z]"
                continue
            res += p[i]

        matches = re.match(res, s)

        if matches and matches.group(0) == s:
            return True

        print(matches.group(1))
        return False

                 

                        
data1="aa"
data2="a*"
c=Solution()
same=c.isMatch(data1,data2)
print(same)