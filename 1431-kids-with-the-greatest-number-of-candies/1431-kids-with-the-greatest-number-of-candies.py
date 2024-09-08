class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=len(candies)
        li=[]
        a=max(candies)
        for i in range(0,l):
            if((candies[i]+extraCandies)>=a):
                li.append(True)
            else:
                li.append(False)
        return li



        