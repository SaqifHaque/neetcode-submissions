class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m, n = 0, 100000
        for num in nums:
            if m < num:
                m = num

        for i in range(1, m):
            if i not in nums:
                return i
        
        return m + 1