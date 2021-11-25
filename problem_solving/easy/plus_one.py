class Solution:
    def plusOne(self, digits: int) -> int:
        digit_len = len(digits)
        l = 1
        result = 0
        index = 0
        while l < digit_len:
            result += digits[index] * 10 **(digit_len - l)
            l+=1
            index += 1
            if index + 1>= digit_len:
                break
        result += digits[-1] + 1
        result = str(result)
        del digits[:]
        for x in result:
            digits.append(int(x))
        return digits    