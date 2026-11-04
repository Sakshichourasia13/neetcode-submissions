class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        has={}
        for i in range(len(s)):
            if s[i] not in has:
                if t[i] in has.values():
                    return False
                has[s[i]]=t[i]
            elif has[s[i]]!=t[i]:
                return False
            
        return True
