class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums) - 1, -1, -1):
            if val == nums[i]:
                nums.pop(i)
            else:
                k += 1

        for i in range(len(nums), len(nums) + (len(nums) - k)):
            nums.append("_")
        
        return k

