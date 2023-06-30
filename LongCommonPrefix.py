''' Leetcode solution to find the Longest Common Prefix 
    Difficulty: Easy 
    Problem Number: 14
    Run time: 47ms 
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key= lambda x: len(x))
        result = ""
        total = 0
        if len(strs) > 0:
            a = strs[0]
            for i in range(len(a)):
                for j in strs[1:]:
                    if a[i] == j[i]:
                        total = total + 1
                if total == len(strs) - 1:
                    result = result + a[i]
                    total = 0
                else:
                    break 
        if len(result) == 0:
            return ""
        else:
            return result 
                
