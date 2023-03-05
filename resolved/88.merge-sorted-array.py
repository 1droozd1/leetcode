#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        j = 0

        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j += 1
            
        lenght = len(nums1)

        for i in range(lenght - 1):
            for j in range(lenght - 1 - i):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
        return(nums1)
           
# @lc code=end