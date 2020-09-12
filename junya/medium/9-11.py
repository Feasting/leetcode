class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ret = [1]
        for i in range(1, target + 1):
            tot = 0
            
            for num in nums:
                if(i - num >= 0):
                    tot += ret[i - num]
                    
            ret.append(tot)
     
        return ret[target]
        
# https://leetcode.com/problems/combination-sum-iv/
