# 9-14-2020
# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        size = len(nums)
        self.index = [0] * size
        if size != 0:
            self.index[0] = nums[0]
            for i in range(1, size):
                self.index[i] += self.index[i-1] + nums[i]
            

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.index[j]
        return self.index[j] - self.index[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
