#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
         
        lenght = len(s)
        stack = []

        for i in range(lenght):

            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                
                if len(stack) == 0:
                    return(False)

                if s[i] == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return(False)
                elif s[i] == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return(False)
                elif s[i] == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return(False)

        if len(stack) == 0:
            return(True)
        else:
            return(False)



        

# @lc code=end