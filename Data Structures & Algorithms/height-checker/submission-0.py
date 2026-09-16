class Solution:
    def heightChecker(self, h: List[int]) -> int:
        s=sorted(h)
        c=0
        for i in range(len(s)):
            if s[i]!=h[i]:
                c+=1
        return c