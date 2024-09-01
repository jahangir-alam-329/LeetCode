class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=len(nums)
        l=[]
        k=[0,0]
        w=-1
        for i in range(0,a):
            if nums[i]==target:
                l.append(i)
        m=len(l)
        if m>=1:
            for p in range(0,1):
                k[0]=l[0]
                k[1]=l[m-1]
            return k
        else:
            for j in range(0,2):
                l.append(w)
            return l
                
                