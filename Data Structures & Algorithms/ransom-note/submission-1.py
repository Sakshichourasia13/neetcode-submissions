class Solution:
    def canConstruct(self, rn: str, mg: str) -> bool:
        h1={}
        h2={}
        for i in rn:
            h1[i]=h1.get(i,0)+1
        for i in mg:
            if i in h1:
                h2[i]=h2.get(i,0)+1
        if len(h1)>len(h2):
            return False
        for i in rn:
            if h1[i]>h2[i]:
                return False
        return True