#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        count = 0
        
        for i in range(len(nums)):
            
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                continue

            nums[count] = nums[i]
            count += 1

        return count
        
# @lc code=end