class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s1=""
        sum=0
        l=len(s)
        d={"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8",
        "i":"9","j":"10","k":"11","l":"12","m":"13","n":"14","o":"15","p":"16",
        "q":"17","r":"18","s":"19","t":"20","u":"21","v":"22","w":"23","x":"24","y":"25","z":"26"
        }
        for i in range(0,l):
            s1=s1+d[s[i]]
        if(k==0):
            return int(s1)
        else:
            l=len(s1)
            for i in range(0,k):
                for j in range(0,l):
                    z=int(s1[j])
                    sum=sum+z
                s1=str(sum)
                sum=0
                l=len(s1)
            return int(s1)
        