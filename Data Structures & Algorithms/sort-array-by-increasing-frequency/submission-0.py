from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        has=Counter(nums)
        return sorted(nums,key=lambda x:(has[x],-x))