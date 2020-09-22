class Solution:

    # TIME EXCEEDED
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        checkDup = set()
        threeSumVec = []
        numsmap = {}
        nums.sort()
        for i in range(len(nums)):
            numsmap[nums[i]] = i
            
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = -(nums[i] + nums[j])
                if sum in numsmap and numsmap[sum] != i and numsmap[sum] != j and numsmap[sum] > j:
                    if (nums[i],nums[j],sum) not in checkDup:
                        threeSumVec.append([nums[i],nums[j],sum])
                    checkDup.add((nums[i],nums[j],sum))
        
        return threeSumVec


    # double pointer with one fixed 
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        threeSumVec = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    threeSumVec.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                        
        return threeSumVec
            