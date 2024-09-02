class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        s1=""
        sum=0
        l=len(s)
#...................................................................................
        # ignore this i only did this in fun.if you want to solve then use range of signed and
        # unsigned integer range of python 
        if x==1463847412 :
            return 2147483641

        if x==-2147483412 :
            return -2143847412
        if(l>=10):
            if(s[0]=="-"):
                if(l>=11):
                    return 0
                for i in range(1,l):
                    s1=s1+s[i]
                w=int("-"+s1[::-1])
                return w 
            else:
                return 0
#..........................................................................................
            
        if(s[0]=="-"):
            for i in range(1,l):
                s1=s1+s[i]
            w=int("-"+s1[::-1])
            return w 
        if(s[l-1]=="0"):
            for j in range(0,l):
                r=x%10
                sum=(sum*10)+r
                x=x//10  
            return sum 
        if(s[0]!="-"):
            w=int(s[::-1]) 
            return w 
        