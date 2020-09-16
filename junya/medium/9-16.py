class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ret = [True]
        for num in nums[:-1]:
            for i in range(0, num - len(ret) + 1):
                ret.append(True)
            ret.pop()
            if not ret:
                return False
        return True
        
# https://leetcode.com/problems/jump-game/
