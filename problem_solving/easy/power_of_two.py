class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        if n == 1:
            return True
            
        while 2**x <= n:
            
            if 2**x == n:
                return True
                break
            x += 1
        
        if 2**x != n:
            return False