#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        def symmet(a, b):

            if not a and not b:
                return True
        
            if not a or not b or a.val != b.val:
                return False
            
            return symmet(a.left, b.right) and symmet(a.right, b.left)
        
        return symmet(root.left, root.right)

        



# @lc code=end