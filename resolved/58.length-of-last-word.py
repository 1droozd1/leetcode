#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while (1):
            try:
                s.index("  ")
                s = s.replace("  ", " ")
            except ValueError:
                
                mas = list(map(str, s.split(" ")))

                if len(mas[0]) == 0:
                    mas = mas[1:]
                if len(mas[-1]) == 0:
                    mas = mas[:len(mas) - 1]
                
                return(len(mas[-1]))
                
# @lc code=end