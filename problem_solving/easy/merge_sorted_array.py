class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        if not m and n:
            del nums2[n:]
            return nums2
        elif not n and m:
            del nums1[m:]
            return nums1
        elif not m and not n:
            return []
        elif bool(m) == True and bool(n)==True:
            
            del nums1[m:]
            del nums2[n:]
            smth = nums1 + nums2
            smth = sorted(smth)
            return smth