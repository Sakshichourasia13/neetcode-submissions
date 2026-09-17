from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        has=Counter(nums)
        n=len(nums)
        return [i for i in has if has[i]>n//3]