class Solution:
    def maxSubArray(self, nums: int) -> int:
        contSum = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)): 
            contSum = max(contSum,currSum)
            if currSum < 0: 
                currSum = 0
            currSum += nums[i]
        return max(contSum,currSum)