class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank={ch:i for i,ch in enumerate(order)}
        if words==sorted(words,key=lambda i: [rank[x] for x in i]):
            return True
        return False
