class Solution:
    def removeDuplicates(self, nums: int) -> int:
        l = 1
        for num in range(1, len(nums)):
            if nums[num] != nums[num - 1]:
                         nums[l] = nums[num]
                         l +=1
        return l