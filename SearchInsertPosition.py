'''Search Insert Position'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        j = 0 
        res = 0 
        while res == 0:
            if target > nums[j]:
                j = j + 1 
            elif target <= nums[j]:
                res = 1 
            if j == len(nums):
                res = 1 
        return j 
        
