#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def hight(self, root):

        if root is None:
            return 0
        else:
            return max(Solution.hight(self, root.left), Solution.hight(self, root.right)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        right_tree = Solution.hight(self, root.right)
        left_tree = Solution.hight(self, root.left)

        if abs(right_tree - left_tree) > 1:
            return False
        
        checking_left = Solution.isBalanced(self, root.left)
        checking_right = Solution.isBalanced(self, root.right)

        if checking_left is True and checking_right is True:
            return True
        else:
            return False


# @lc code=end