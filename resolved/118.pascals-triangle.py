#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        
        all_lists_array = [[1], [1, 1]]
        stroka = 3

        while stroka <= numRows:
            strok_array = [0] * stroka
            strok_array[0], strok_array[-1] = 1, 1

            for i in range(1, stroka - 1):
                strok_array[i] = all_lists_array[stroka - 2][i - 1] + all_lists_array[stroka - 2][i]
            all_lists_array.append(strok_array)
            stroka += 1
        
        return(all_lists_array)
# @lc code=end