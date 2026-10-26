class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        has={}
        for i in s1.split():
            has[i]=has.get(i,0)+1
        for i in s2.split():
            has[i]=has.get(i,0)+1
        return [i for i in has if has[i]==1]
