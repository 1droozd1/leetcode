#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        massive = [0] * 46
        massive[0] = 1
        massive[1] = 1

        for i in range(2, len(massive)):
            massive[i] = massive[i - 1] + massive[i - 2]
        return(massive[n])

# @lc code=end