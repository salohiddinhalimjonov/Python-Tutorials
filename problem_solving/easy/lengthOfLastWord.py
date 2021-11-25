class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_words = s.strip()
        list_words = list_words.split(" ")
        last_word = list_words[-1]
        return len(last_word)