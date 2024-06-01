class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        l=['0']*len(s)
        for ind,i in enumerate(s):
            if i=='(':
                stack.append(ind)
            else:
                if stack:
                    l[stack.pop()]='1'
                    l[ind]='1'
        return max(len(i) for i in ''.join(l).split('0'))