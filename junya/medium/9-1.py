class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prevList = [1]
        postList = [1]
        revNums = nums[::-1]
        
        for num in range(0, len(nums) - 1):
            prevList.append(prevList[-1] * nums[num])
        
        for num in range(0, len(nums) - 1):
            postList.append(postList[-1] * revNums[num])
            
        ret = []
        postList.reverse()
        for i in range (0, len(nums)):
            print(i)
            ret.append(prevList[i] * postList[i])
        
        return ret
        
# https://leetcode.com/problems/product-of-array-except-self/
