class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count =0
        arr= list(s)
        for i in range(len(arr)):
            if arr[i]=='(':
                count+=1
            elif arr[i]==')':
                if count==0:
                    arr[i]='*'
                else:
                    count -=1
        for i in range(len(arr)-1,-1,-1):
            if count>0 and arr[i]=='(':
                arr[i]='*'
                count-=1
        result=''.join(c for c in arr if c !='*')
        return result