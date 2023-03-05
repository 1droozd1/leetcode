#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
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
        while (n.next):
            n = n.next
        n.next = end

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None or list2 is None:
            if list2 is None:
                return (list1)
            else:
                return(list2)
            

        merge_mass = [list1.val, list2.val]

        while list1.next:
            list1 = list1.next
            merge_mass.append(list1.val)
            

        while list2.next:
            list2 = list2.next
            merge_mass.append(list2.val)
            
        merge_mass.sort()
        
        list3 = ListNode(merge_mass[0])

        for i in range(1, len(merge_mass)):
            list3.appending(merge_mass[i])
        
        return(list3)

# @lc code=end