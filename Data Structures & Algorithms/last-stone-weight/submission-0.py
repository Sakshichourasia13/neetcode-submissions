class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            x,y=stones[-2],stones[-1]
            if x==y:
                stones.pop(-1)
                stones.pop(-1)
            else:
                stones.pop(-1)
                stones[-1]=y-x
        return stones[0] if stones else 0