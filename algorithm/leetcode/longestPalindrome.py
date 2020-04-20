class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        if len(s)==1:
            return s

        longest = 0
        out_l = 0
        out_r = 0
        for i in range(1, len(s)):
            print(i)
            if s[i] == s[i-1]: # abba
                palindrome_l, palindrome_r = self.find_palindrome(s, i-1, i)
                if palindrome_r - palindrome_l + 1 > longest:
                    longest = palindrome_r - palindrome_l + 1
                    out_l = palindrome_l
                    out_r = palindrome_r

            if i>1 and s[i] == s[i-2]: # ababa
                palindrome_l, palindrome_r = self.find_palindrome(s, i-2, i)
                print(palindrome_l, palindrome_r)
                if palindrome_r - palindrome_l + 1 > longest:
                    longest = palindrome_r - palindrome_l + 1
                    out_l = palindrome_l
                    out_r = palindrome_r

        return s[out_l:out_r+1]

    def find_palindrome(self,s, l, r):
        while l-1 >= 0 and r+1 < len(s):
            if s[l-1] != s[r+1]:
                break
            l-=1
            r+=1
        return l,r

def main():
    s = Solution()
    ans = s.longestPalindrome("babad")
    print(ans)

# 已经写傻了
class SolutionNotWorking:
    def longestPalindrome(self, s: str) -> str:
        if len(s)< 2:
            return s
        last_start = 0
        last_end = 0
        sub_start = 0
        sub_end = 0
        
        if len(s)==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        
        for idx,val in enumerate(s):
            if idx<2:
                continue
            #same char in row
            previous=idx
            while True:
                previous -=1
                
                if s[previous] != val:
                    sub_start = previous+1
                    sub_end = idx
                    
                    if sub_end-sub_start>last_end-last_start:
                        last_start = sub_start
                        last_end = sub_end
                    
                    break
                    
                if previous == 0:
                    sub_start = 0
                    sub_end = idx
                    if sub_end-sub_start>last_end-last_start:
                        last_start = sub_start
                        last_end = sub_end
                    break
                    
            loop = True
            if s[idx-2] == val:
                sub_start = idx-2
                sub_end = idx
                palindromic_idx_right = idx
                palindromic_idx_left = idx -2
            elif s[idx-1] == val:
                sub_start = idx-1
                sub_end = idx
                palindromic_idx_right = idx
                palindromic_idx_left = idx -1
            else:
                loop = False
                
            while loop:
                palindromic_idx_right+=1
                palindromic_idx_left-=1
                if palindromic_idx_right>=len(s):
                    break
                if palindromic_idx_left<0:
                    break
                print('left right',s[palindromic_idx_right] , s[palindromic_idx_left])
                print('--left right',palindromic_idx_right , palindromic_idx_left)
                if s[palindromic_idx_right] == s[palindromic_idx_left]:
                    sub_start = palindromic_idx_left
                    sub_end = palindromic_idx_right
                else:
                    break
            
            if sub_end-sub_start>last_end-last_start:
                last_start = sub_start
                last_end = sub_end
                
        if s[0]==s[1]:
            if last_end-last_start<2:
                last_start = 0
                last_end = 1
                
        return s[last_start:last_end+1]
        
#     def _is_palindromic(sub_str)
#         flag = True
#         if len(sub_str) % 2 ==0:
#             mid_idx = len(sub_str)//2+1
#         else:
#             mid_idx = len(sub_str)//2
            
#         for i in range(mid_idx):
#             if sub_str[i]!=sub_str[-i]
#                 flag = False
#                 break
                
#         return flag
                
if __name__ == '__main__':
    main()