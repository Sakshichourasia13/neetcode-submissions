class Solution:
    def maxProfit(self, p: List[int]) -> int:
        mn=float('inf')
        ans=0
        for i in p:
            mn=min(mn,i)
            ans=max(ans,i-mn)
        return ans