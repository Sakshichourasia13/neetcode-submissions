class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=strs[0]
        for i in strs[1:]:
            j=0
            while j<min(len(s),len(i)):
                if s[j]!=i[j]:
                    break
                j+=1
            s=s[:j]
        return s
                