class Solution:
    def romanToInt(self, s: str) -> int:
        roman_table = {
            "I": 1,
            "V":5,
            "X":10,
            "L": 50,
            "C": 100,
            "D":500,
            "M":1000

        }
        num = 0
        last = "I"
        for roman in s[::-1]:
            if roman_table[roman] < roman_table[last]:
                num -= roman_table[roman]
            else:
                num += roman_table[roman]
            last = roman   
        return num   