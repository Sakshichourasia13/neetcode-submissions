from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        has=Counter(words[0])
        for i in words:
            h2=Counter(i)
            for j in has:
                has[j]=min(has[j],h2[j])
        ans=[]
        for i in has:
            ans.extend(list(i*has[i]))
        return ans
