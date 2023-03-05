#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        rowIndex += 1
        if rowIndex == 1:
            return [1]
        
        all_lists_array = [[1], [1, 1]]
        stroka = 3

        while stroka <= rowIndex:
            strok_array = [0] * stroka
            strok_array[0], strok_array[-1] = 1, 1

            for i in range(1, stroka - 1):
                strok_array[i] = all_lists_array[stroka - 2][i - 1] + all_lists_array[stroka - 2][i]
            all_lists_array.append(strok_array)
            stroka += 1
        
        return(all_lists_array[-1])
    
# @lc code=end