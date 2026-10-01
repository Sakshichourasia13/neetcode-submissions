class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for i in words:
            g=True
            for j in i:
                if j not in allowed:
                    g=False
                    break
            if g:
                c+=1
        return c
                