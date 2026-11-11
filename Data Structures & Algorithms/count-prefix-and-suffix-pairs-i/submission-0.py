class Solution:
    def isPrefixAndSuffix(self,s1,s2):
        if s2.startswith(s1) and s2.endswith(s1):
            return True
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if self.isPrefixAndSuffix(words[i],words[j]):
                    c+=1
        return c
