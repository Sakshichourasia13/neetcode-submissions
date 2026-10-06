from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        has=Counter(s)
        mx,mn=0,float('inf')
        for i in has:
            if mx<has[i] and has[i]%2:
                mx=has[i]
            elif mn>has[i] and has[i]%2==0:
                mn=has[i]
        return mx-mn