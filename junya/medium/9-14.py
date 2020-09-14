class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        curr1 = 0
        prev2 = 0
        curr2 = 0
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        nums1 = nums.copy()
        nums1.pop()
        nums2 = nums.copy()
        nums2.pop(0)
        
        for num in nums1:
            temp = curr1
            curr1 = max(prev1 + num, curr1)
            prev1 = temp
        
        for num in nums2:
            temp = curr2
            curr2 = max(prev2 + num, curr2)
            prev2 = temp
            
        return max(curr1, curr2)
        
# https://leetcode.com/problems/house-robber-ii/
