class Solution:
    def isValid(self, s):
        brac_dict= {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []
        for char in s:
            if char in brac_dict:
                if stack and stack[-1] == brac_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack  else False
s = '(){}[]'
sol = Solution()
res = sol.isValid(s)
print(res)