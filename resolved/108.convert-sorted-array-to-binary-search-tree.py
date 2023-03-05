#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
            


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        mid_elem = len(nums) // 2

        root = TreeNode(nums[mid_elem])

        root.left = Solution.sortedArrayToBST(self, nums[:mid_elem])
        root.right = Solution.sortedArrayToBST(self, nums[mid_elem + 1:])

        return root


        
# @lc code=end