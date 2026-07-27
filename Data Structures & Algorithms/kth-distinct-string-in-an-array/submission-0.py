class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        has={}
        n=0
        for i in arr:                
            has[i]=has.get(i,0)+1
        print(has)

        for i in has:
            if has[i]==1:
                n+=1
            if n==k:
                return i
        

        return ""
