class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        if len(nums) < 3:
            return ret
        
        prev = nums[0]
        for a in range(0, len(nums) - 1):
            if prev == nums[a] and a != 0:
                continue
            
            b = a+1
            c = len(nums) - 1
            
            while(b != c):
                tot = nums[b] + nums[c]
                if nums[a] + tot == 0:
                    ret.append([nums[a], nums[b], nums[c]])
                    b += 1
                    while nums[b - 1] == nums[b]:
                        if b < c:
                            b += 1
                        else:
                            break
                elif nums[a] + tot < 0:
                    b += 1
                else:
                    c -= 1
                    
            prev = nums[a]
        return ret
        
# https://leetcode.com/problems/3sum/
