class Solution:
    def vowelStrings(self, w: List[str], queries: List[List[int]]) -> List[int]:
        ans=[]
        for l,r in queries:
            a=0
            for i in range(l,r+1):
                if w[i][0] in 'aeiou' and w[i][-1] in 'aeiuo':
                    a+=1
            ans.append(a)
        return ans