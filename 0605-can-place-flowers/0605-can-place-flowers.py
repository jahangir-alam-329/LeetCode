class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l=len(flowerbed)
        if l==1:
            if flowerbed[0]==1 and n>=1:
                return False
            else:
                return True
        t=n
        if(flowerbed[0]==0 and flowerbed[1]==0):
            t=t-1
            flowerbed[0]=1
        for i in range(1,l-1):
            if flowerbed[i]==0:
                if(flowerbed[i-1]==0 and flowerbed[i+1]==0):
                    t=t-1
                    flowerbed[i]=1
        if(flowerbed[l-1]==0 and flowerbed[l-2]==0):
            flowerbed[l-1]=1
            t=t-1
        if t==0:
            return True
        else:
            return False

        