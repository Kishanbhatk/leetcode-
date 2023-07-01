''' Leetcode solution to check the valid parenthesis 
    Problem Number : 20
    Run time : 51ms 
'''


class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {"{":"}","[":"]","(":")","]":"[","}":"{",")":"("}
        stack = []
        j = 0
        for i in s:
            if i in "{[(" or len(stack) == 0:
                stack.append(i)
            elif i in "]})":
                if dictionary[stack[-1]] == i:
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False
