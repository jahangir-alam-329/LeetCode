class Solution:
    def reverseWords(self, s: str) -> str:
        
        x = s.split()
        l=len(x)
        print(x[0])
        l=l-1
        t=""
        while(l>=0):
            t=t+" "+x[l]
            l=l-1
        t = t.strip()
        return t
        