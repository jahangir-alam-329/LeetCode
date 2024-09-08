class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w3=""
        l=len(word1)
        l2=len(word2) 
        if(l<l2):
            w4=word2[slice(l,l2)]
            l=l
        else:
            w4=word1[slice(l2,l)]
            l=l2
        for i in range(0,l):
            w3=w3+word1[i]+word2[i]
        w3=w3+w4
        return w3
        