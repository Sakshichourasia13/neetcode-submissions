class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=[i*i for i in nums]
        return sorted(s)