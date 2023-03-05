#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clear_str = ''
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyz":
                clear_str += i
        print(clear_str)


# @lc code=end