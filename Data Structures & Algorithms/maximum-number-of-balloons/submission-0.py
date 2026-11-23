class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        has={}
        for i in text:
            if i in 'balon':
                has[i]=has.get(i,0)+1
        if len(has)<5:
            return 0

        has['l']//=2
        has['o']//=2
        return min(has.values())