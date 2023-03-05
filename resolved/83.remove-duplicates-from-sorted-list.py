#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def appending(self, val):
        end = ListNode(val)
        n = self
        while(n.next):
            n = n.next
        n.next = end

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return(head)
        
        massive = [head.val]
        while head.next:
            head = head.next        
            massive.append(head.val)

        massive = sorted(list(set(massive)))

        result_list = ListNode(massive[0])
        
        for i in range(1, len(massive)):
            result_list.appending(massive[i])
        
        return(result_list)
# @lc code=end