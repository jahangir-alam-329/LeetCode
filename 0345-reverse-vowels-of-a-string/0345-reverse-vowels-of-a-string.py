class Solution:
    def reverseVowels(self, s: str) -> str:
        
        str1=[]
        for k in s:
            str1.append(k)
            vowel="aeiouAEIOU"
        l=len(str1)
        lastindex=l-1
        m=""
        n=""
        for i in range(0,l):
            if (str1[i] in vowel) and (i<lastindex):
                for j in range(i,lastindex+1):
                    if str1[lastindex] in vowel:
                        m=str1[i]
                        n=str1[lastindex]
                        str1[lastindex]=m
                        str1[i]=n
                        lastindex=lastindex-1
                        break
                    else:
                        lastindex=lastindex-1
        t=""
        for i in range(0,l):
            t=t+str1[i]
        return t


            
        