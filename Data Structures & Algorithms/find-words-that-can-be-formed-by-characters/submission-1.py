class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        has=Counter(chars)
        ans=0
        b=True
        for i in words:
            temp=has.copy()
            for j in i:
                if j not in temp or temp[j]==0:
                    b=False
                    break
                temp[j]-=1
                b=True
            if b:
                ans+=len(i)
        return ans