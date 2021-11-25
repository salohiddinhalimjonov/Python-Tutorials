# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)-1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return ([i, j])
class Solution:
    def twoSum(self, nums, target: int):
        value = {}
        for index_ , num1 in enumerate(nums):
            num2 = target - num1
            if num2 in value.keys():
                return [value[num2], index_]
            elif num1 not in value:
                value[num1] = index_