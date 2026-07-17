class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        maxVal = 0
        maxRes = 0

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        if len(hashmap) == 0:
            return maxRes
        
        for i, val in enumerate(hashmap):
            if maxRes <= hashmap[val]:
                maxVal = val
                maxRes = hashmap[val]
        
        return maxVal