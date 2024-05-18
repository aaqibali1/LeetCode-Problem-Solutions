class Solution:
    def countDigitOne(self, n: int) -> int:
        nst=str(n)
        s=0
        ln=len(nst)
        if(n<10):
            if(n==0):
                return 0
            else:
                return 1
        for i in range(ln):
            if(nst[i]=="0"):
                x=str(int(nst[:i])-1)+(ln-i-1)*"9"
            elif(nst[i]=="1"):
                x=nst[:i]+nst[i+1:]
            else:
                x=nst[:i]+(ln-i-1)*"9"
            # print(x)
            if(x==""):
                continue
            s+=int(x)+1
        return(s)