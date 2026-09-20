class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        i,j=0,0
        ans=""
        while i<len(w1) and j<len(w2):
            ans+=w1[i]
            ans+=w2[j]
            i+=1
            j+=1
        if i<len(w1):
            ans+=w1[i:]
        elif j<len(w2):
            ans+=w2[j:]
        return ans