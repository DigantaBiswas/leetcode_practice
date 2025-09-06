class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        j = 0
        for c in s:
            while j < len(t) and j < len(t):
                if t[j] == c:
                    j = j + 1
                    s_len -= 1
                    if s_len == 0:
                        return True
                    break
                j+=1
        return True if s_len == 0 else False

        