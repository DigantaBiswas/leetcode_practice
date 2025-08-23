class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ["a", "e", "i", "o", "u"]
        vowel_indx = []
        vowels = []
        s = list(s)
        for i in range(0, len(s)):
            if s[i].lower() in v:
                vowel_indx.append(i)
                vowels.append(s[i])
        for j in vowel_indx:
            s[j] = vowels.pop()
        return "".join(s)
        