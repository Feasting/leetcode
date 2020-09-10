class Solution:
    def containsDuplicate(self, nums) -> bool:
        set1 = set()
        for i in range(len(nums)):
            if nums[i] in set1:
                return True
            set1.add(nums[i])
        
        return False