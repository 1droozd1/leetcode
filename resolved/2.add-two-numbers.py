#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        end = ListNode(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        sum1 = l1.val
        kf1 = 10
        while l1.next:
            l1 = l1.next
            sum1 += l1.val * kf1
            kf1 *= 10

        sum2 = l2.val
        kf2 = 10
        while l2.next:
            l2 = l2.next
            sum2 += l2.val * kf2
            kf2 *= 10
        
        all_sum = sum1 + sum2
        l3 = ListNode(all_sum % 10)
        all_sum //= 10

        while(all_sum > 0):
            l3.append(all_sum % 10)
            all_sum //= 10
        
        return(l3)
        
# @lc code=end