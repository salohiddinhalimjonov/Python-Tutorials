class Solution:
    def searchInsert(self, nums: int, target: int) -> int:
        for x in nums:
            if target in nums:
                index_ = nums.index(target)
                return index_
            elif target not in nums and x > target:
                index_ = nums.index(x)
                if index_ == 0:
                    return 0
                elif index_ > 0:
                    return index_ - 1
            elif target not in nums and target > nums[-1]:
                return len(nums)
            y = 0
            while target > nums[y]:
                y += 1
                if target < nums[y]:
                    return y