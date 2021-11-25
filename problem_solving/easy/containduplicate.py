class Solution:
    def containsDuplicate(self, nums) -> bool:
        s = set(nums)
        return len(s) != len(nums)

