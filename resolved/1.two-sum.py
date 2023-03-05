#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        leng = len(nums)
        for i in range(leng - 1):
            for j in range(i + 1, leng):
                if nums[i] + nums[j] == target:
                    return([i, j])
             


# @lc code=end