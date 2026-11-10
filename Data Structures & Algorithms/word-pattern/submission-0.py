class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        s=s.split(" ")
        if len(p)!=len(s):
            return False
        h1={}
        h2={}
        print()
        for i in range(len(p)):
            if p[i] in h1 and h1[p[i]]!=s[i]:
                return False
            if s[i] in h2 and h2[s[i]]!=p[i]:
                return False

            h1[p[i]]=s[i]
            h2[s[i]]=p[i]
        return True