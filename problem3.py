class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        char_list=[]
        if s==" ":
            return 1
        if len(s)==1:
            return 1
        for str in s:
            if str not in char_list:
                char_list.append(str)
                if count< len(char_list):
                    count=len(char_list)
            else:
                while str in char_list:
                    char_list.pop(0)
                char_list.append(str)
                if count< len(char_list):
                    count=len(char_list)
        return count



