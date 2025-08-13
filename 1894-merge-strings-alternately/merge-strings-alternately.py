class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word=""
        word1 = list(word1)
        word2 = list(word2)

        min_len = len(word1) if len(word1) < len(word2) else len(word2)
        for i in range (0, min_len):
            new_word += word1.pop(0)
            new_word += word2.pop(0)

        new_word += "".join(word1)
        new_word += "".join(word2)
        return new_word



        
        



        