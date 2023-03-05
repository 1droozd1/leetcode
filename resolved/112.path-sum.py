#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def preorder (self, root, summ, array):
        if root:
            summ += root.val
            if root.right is None and root.left is None:
                array.append(summ)
            TreeNode.preorder(self, root.left, summ, array)
            TreeNode.preorder(self, root.right, summ, array)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        summ = 0
        array = []

        TreeNode.preorder(self, root, summ, array)
        
        if targetSum in array:
            return True
        else:
            return False
        
# @lc code=end