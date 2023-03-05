#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        count = 0

        for i in range(len(nums)):

            if nums[i] == val and i <= len(nums) - 1:
                continue

            nums[count] = nums[i]
            count += 1
        
        return(count)
            
        
# @lc code=end