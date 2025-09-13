class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        vowels = "aeiouAEIOU"
        for i in range(0, k):
            if s[i] in vowels:
                max_vowels += 1
        j = k
        cur_vowels = max_vowels
        for j in range(j, len(s)):
            if s[j] in vowels:
                cur_vowels += 1
            if s[j-k] in vowels:
                cur_vowels -= 1
            if max_vowels<cur_vowels:
                max_vowels = cur_vowels

        return max_vowels

        