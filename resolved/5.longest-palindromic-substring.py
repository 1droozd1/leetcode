#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        max_len = ''
        lenght = len(s)

        for i in range(lenght - 1):

            max_palinsdr = s[i]
            j = i + 1

            while j < lenght:
                max_palinsdr += s[j]
                j += 1
                if max_palinsdr == max_palinsdr[::-1]:
                    if len(max_len) < len(max_palinsdr):
                        max_len = max_palinsdr
        
        if len(max_len) == 0:
            return (s[0])
        
        return(max_len)

# @lc code=end