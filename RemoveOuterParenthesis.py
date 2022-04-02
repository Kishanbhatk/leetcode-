'''Leetcode Problem to remove the Outer parenthesis of a valid parenthesis string
   ex: s = Input: s = "(()())(())"
                  Output: "()()()" '''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        j = 0 
        stack = []
        stack1 = []
        k = 0 
        
        for i in range(0,len(s)):
            if i == 0:
                stack.append(s[i])
                j = j + 1
            else:
                if not stack:
                    stack1.append(s[k+1:i-1])
                    k = i 
                if i == len(s) - 1:
                    stack1.append(s[k+1:i])
                if s[i] == "(":
                    stack.append(s[i])
                    j = j + 1
                else:
                    stack.pop()
                    j = j - 1
        return "".join(stack1)
        
