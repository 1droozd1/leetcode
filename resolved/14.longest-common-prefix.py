#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        lenght = len(strs)
        kf = 0
        j = 1
        first_el = strs[0]

        while(kf == 0):

            literal = first_el[0:j]

            for i in range(1, lenght):
                second_el = strs[i]
                if second_el[0:j] != literal:
                    kf = 1
                    break

            j += 1

            if literal == first_el:
                break
        

        if kf == 1:
            all_prefix = literal[:len(literal) - 1]
        else:
            all_prefix = literal
        
        return(all_prefix)

# @lc code=end