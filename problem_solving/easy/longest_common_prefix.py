class Solution:
    def longestCommonPrefix(self, strs) -> str:
        dict_strs = {}
        length = len(strs)
        if not length:
            return ""
        elif length == 1:
            return strs[0]
        string1 = strs[0]
        str_len = len(string1)
        for string_ in strs[1:]:
            while string1 != string_[0:str_len]:
                string1 = string1[0:str_len-1]
                str_len -= 1
                if str_len == 0:
                    return ''
        return string1     