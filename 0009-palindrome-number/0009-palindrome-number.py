class Solution:
    def isPalindrome(self, x: int) -> bool:
        sum=0
        p=str(x)
        q=x
        l=len(p)
        if(p[0]!="-"):
            for i in range(0,l):
                r=x%10
                sum=(sum*10)+r
                x=x//10
            if(sum==q):
                return True
            else:
                return False
        else:
            return False