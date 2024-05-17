class Solution:
    def removeDuplicates(self, s: str) -> str:
        sta = [] 
        for c in s : 
            if sta and sta[-1] == c :
                sta.pop()
            else :
                sta.append(c)
        return ''.join(sta)