class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        majority = len(nums) / 3
        res = []

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        
        for k, v in hashmap.items():
            if v > majority:
                res.append(k)
        
        return res