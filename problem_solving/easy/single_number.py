class Solution:
    def singleNumber(self, nums) -> int:
        dict1 = {}
        for index_, num in enumerate(nums):
            if num not in dict1:
                dict1[num] = index_
            elif num in dict1:
                dict1.pop(num)
        a = 0        
        for z in dict1.keys():
            a = z
        return a    