# 9-4-2020
# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        result = []
        print(counts)
        for i in range(k):
            high = float('-inf')
            high_value = float('-inf')
            for num in counts:
                if counts[num] > high_value:
                    high = num
                    high_value = counts[num]
            counts[high] = float('-inf')
            result.append(high)
        return result
