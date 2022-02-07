'''The Leetcode solution for the Longest common prefix problem'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        s = [] 
        for i in range(0,len(strs)):
            if i == 0:
                s.append(strs[i])
            else:
                j = 0 
                lens_min = min(len(s[0]),len(strs[i]))
                while(j<lens_min and (s[0][j] == strs[i][j])):
                    j = j + 1 
                if j > 0:
                    c = s.pop()
                    s.append(c[0:j])
                else:
                    s.pop()
                    break
        if len(s) == 0:
            return ""
        else:
            return s[0]
