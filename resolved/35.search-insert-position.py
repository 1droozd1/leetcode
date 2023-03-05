#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        try: 
            return(nums.index(target))

        except ValueError:
            for i in range(len(nums)):
                if target <= nums[i]:
                    return(i)
            return(len(nums))

# @lc code=end