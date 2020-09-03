class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leng = 0
        for i in range(1, len(nums)):
            if nums[leng] != nums[i]:
                nums[leng + 1] = nums[i]
                leng += 1
        leng += 1
        return leng
        
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
