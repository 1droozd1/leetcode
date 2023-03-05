#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
 
        return(list(int(char) for char in str(int("".join(list(str(i) for i in digits))) + 1)))

# @lc code=end