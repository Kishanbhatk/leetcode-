'''String to Integer'''
import string
class Solution:
    def myAtoi(self, s: str) -> int:
        maxsize = 2**31 - 1
        minsize = -(2**31)
        
        result = 0 
        
        if not s:
            return 0 
        i = 0
        while i<len(s) and s[i] == " ":
            i = i + 1
        sign = 1
        
        if i<len(s) and s[i] == '+':
            i = i + 1
        elif i<len(s) and s[i] == '-':
            sign = -1
            i = i + 1
        while(i< len(s) and s[i]>= '0' and s[i]<='9'):
            if result > (maxsize - int(s[i]))/10 :
                return maxsize if sign > 0 else minsize
            else:
                result = result * 10 + int(s[i])
                i = i + 1
        return sign * result 
            
