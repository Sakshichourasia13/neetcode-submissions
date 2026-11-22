class Solution:
    def maxScore(self, s: str) -> int:
        if '1' not in s or '0' not in s:
            return len(s)-1
        r=s.count('1')
        mx=0
        l=0
        for i in range(len(s)-1):
            if s[i]=='0':
                l+=1
            else:
                r-=1
            mx=max(l+r,mx)
        return mx