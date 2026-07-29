class Solution:
    def check(self, nums: List[int]) -> bool:
        mn=nums.index(min(nums))
        return nums[mn:]+nums[:mn]==sorted(nums)