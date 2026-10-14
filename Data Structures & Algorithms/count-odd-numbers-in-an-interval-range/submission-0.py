class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if high%2 or low%2:
            n=1
        else:   n=0
        return ((high-low)//2+n)