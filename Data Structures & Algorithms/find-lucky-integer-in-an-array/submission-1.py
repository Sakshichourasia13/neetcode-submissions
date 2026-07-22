class Solution:
    def findLucky(self, arr: List[int]) -> int:
        has={}

        for i in arr:
            has[i]=has.get(i,0)+1
        c=0
        for i in has:
            if has[i]==i:
                c=max(c,i)
        return c if c else -1