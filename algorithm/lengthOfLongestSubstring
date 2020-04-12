class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_start=0
        sub_end=1
        longest=1
        
        if len(s) < 1:
            return 0
        
        while True:
            if sub_end >= len(s):
                break
            
            if s[sub_end] in s[sub_start:sub_end]:
                sub_start += s[sub_start:sub_end].index(s[sub_end])+1
                sub_end += 1
            else:
                sub_end += 1
                length = sub_end-sub_start
                if length > longest:
                    longest = length
        
        return longest
