class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        a = 1
        while a * a < x:
            a +=1
            if a *a == x:
                return a
            elif a * a > x:
                return a -1
                