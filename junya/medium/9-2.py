class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr = nums[0]
        posi = nums[0]
        neg = nums[0]
        
        newNums = nums[1:]
        for num in newNums:
            temp = [posi*num, neg*num, num]
            posi = max(temp)
            neg = min(temp)
            curr = max([posi, neg, curr])
            
        return curr
        
# https://leetcode.com/problems/maximum-product-subarray/
