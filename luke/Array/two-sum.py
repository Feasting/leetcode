class Solution:
    def twoSum(self, nums, target):

        # brutaforcsu
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i, j]
                

        # hashumapu
        numsmap = {}
        for i in range(len(nums)):
            numsmap[nums[i]] = i
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numsmap and numsmap[comp] != i:
                return [i, numsmap[comp]]