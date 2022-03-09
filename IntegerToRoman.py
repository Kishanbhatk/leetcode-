'''Interger to Roman Conversion'''

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        l1 = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        l2 = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        for i in range(len(l1)):
            while num >= l1[i]:
                ans = ans + l2[i]
                num = num - l1[i]
        return ans 
        
