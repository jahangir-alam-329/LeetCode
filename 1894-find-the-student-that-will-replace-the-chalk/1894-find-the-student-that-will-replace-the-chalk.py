class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        l=len(chalk)
        sum=0
        s1=0
        w=1
        l=len(chalk)

        if(l==1):
            return 0
            
        for j in range(0,l):
            sum=sum+chalk[j]
        while(s1<k):
            s1=sum*w
            w=w+1
        k=k-(s1-sum)
        i=0
        if(k==0):
            return 0

        for i in range(0,l):
            k=k-chalk[i]
            if(k==0):
                if(i==(l-1)):
                    return 0
                else:
                    return i+1
            if(k<chalk[i+1]):
                return i+1
            











        # while(k != 0):
        #     if(k >=chalk[i]):
        #         k=k-chalk[i]
        #     if(k==0):
        #         if(i==l-1):
        #             return 0
        #         else:
        #             return i+1
        #     if(k<chalk[i]):
        #         if(i==l-1):
        #             return 0
        #         else:
        #             return i+1
        #         #return i+1
        #     if(k<chalk[0]):
        #         return l-1
        #     if(i<l-1):
        #         i=i+1
        #     else:
        #         i=0
    
        