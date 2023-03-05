#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        right_tree = Solution.minDepth(self, root.right)
        left_tree = Solution.minDepth(self, root.left)
        
        if root.right is None:
            return left_tree + 1
        
        if root.left is None:
            return right_tree + 1
        
        return min(right_tree, left_tree) + 1

# @lc code=end