from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        has=Counter(s)
        s="".join(sorted(s,key=lambda x:has[x],reverse=True))
        return s