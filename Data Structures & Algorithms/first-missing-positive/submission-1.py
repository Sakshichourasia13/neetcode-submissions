from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        has=Counter(nums)
        mx=max(nums)
        if mx<=0:
            return 1
        for i in range(1,mx):
            if i not in has:
                return i
        return mx+1