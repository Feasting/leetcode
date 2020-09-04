class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dpArray = [nums[0]]
        
        # binary search
        def BSHelper(num, anArr, start, end):
            if start == end:
                return end
            if (end-start)%2 == 0:
                mid = (end-start)//2 + start
            else:
                mid = (end-start-1)//2 + start
            
            if num < anArr[mid]:
                return BSHelper(num, anArr, start, mid)
            elif num > anArr[mid]:
                return BSHelper(num, anArr, mid+1, end)
            else:
                return mid
        
        leng = len(dpArray)
        for num in nums[1:]:
            ind = BSHelper(num, dpArray, 0, leng)
            if ind == len(dpArray):
                dpArray.append(num)
                leng += 1
            else:
                dpArray[ind] = num
                
        return leng
        
# https://leetcode.com/problems/longest-increasing-subsequence/
