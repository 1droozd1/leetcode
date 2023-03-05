#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return(False)
        else:
            string = str(x)
            string = string[::-1]
            
            if int(string) == x:
                return(True)
            else:
                return(False)


# @lc code=end