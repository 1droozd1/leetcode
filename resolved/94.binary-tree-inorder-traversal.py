#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

        def in_order(node, result_mas):
            if node:
                in_order(node.left, result_mas)
                result_mas.append(node.val)
                in_order(node.right, result_mas)

        result_mas = list()
        in_order(root, result_mas)
        
        return(result_mas)

# @lc code=end