class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = 0
        if bool(needle) == False:
            return 0
        elif bool(needle) == True and needle not in haystack:
            return -1
        elif bool(needle) == True and needle in haystack:
            index_ = haystack.index(needle)
            return index_
        