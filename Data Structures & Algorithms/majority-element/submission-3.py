class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        maxRes = 0
        maxVal = 0

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
            if hashmap[num] > maxVal:
                maxVal = hashmap[num]
                maxRes = num
        return maxRes

        
        
        