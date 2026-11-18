class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if nums==sorted(nums)[::-1]:
            return max(nums)
        sm=nums[0]
        mx=0
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                sm+=nums[i]
            else:
                sm=nums[i]
            mx=max(mx,sm)
        return mx