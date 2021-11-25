class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # if s == " ":
        #     return True
        result = ""
        for z in s:
            if z.isalpha():
                result+=z.lower()
            elif z.isnumeric():
                result += z
        return result == result[::-1]