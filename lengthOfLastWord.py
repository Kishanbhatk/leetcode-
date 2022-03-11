'''lengthOfLastWord'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = 0 if len(s.strip()) == 0 else s.strip().split(" ")
        if x == 0:
            return 0
        else:
            return len(x[-1])
        
