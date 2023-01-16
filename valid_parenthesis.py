class Solution:
    def isValid(self, s: str) -> bool:
        result = True
        stack = []
        for paren in s:
            if paren in ["(", "{", "["]:
                stack.append(paren)
            else:
                if not stack:
                    result = False
                else:
                    if stack[-1] == "(" and paren == ")" or stack[-1] == "{" and paren == "}" or stack[-1] == "[" and paren == "]":
                        stack.pop(-1)
                    else:
                        result = False
        if stack:
            result = False
        return result


# result = Solution().isValid("()[]{}")
# print(result)
#
# result = Solution().isValid("({})[}")
# print(result)

result = Solution().isValid("(])")
print(result)
