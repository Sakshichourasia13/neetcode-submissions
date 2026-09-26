from math import floor
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            i=gifts.index(max(gifts))
            gifts[i]=floor(gifts[i]**(0.5))
        return sum(gifts)