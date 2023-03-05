#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        size_nums1 = len(nums1)
        size_nums2 = len(nums2)
        all_lenght = size_nums1 + size_nums2
        merging_array = []

        i, j = 0, 0

        while i < size_nums1 or j < size_nums2:

            if i < size_nums1 and j < size_nums2:
                if nums1[i] < nums2[j]:
                    merging_array.append(nums1[i])
                    i += 1
                else:
                    merging_array.append(nums2[j])
                    j += 1
            elif i < size_nums1:
                merging_array += nums1[i:]
                break
            elif j < size_nums2:
                merging_array += nums2[j:]
                break
        
        if all_lenght % 2 == 0:
            return float((merging_array[all_lenght // 2 - 1] + merging_array[all_lenght // 2]) / 2)
        else:
            return float(merging_array[all_lenght // 2])

# @lc code=end