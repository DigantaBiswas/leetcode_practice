class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        if str1 + str2 == str2 + str1:
            a = len(str1)
            b = len(str2)

            if a > b:
                l = a
                s = b
            else:
                l = b
                s = a
            while s != 0:
                l, s = s, l % s
            gcd = str1[:l]
        return gcd
        