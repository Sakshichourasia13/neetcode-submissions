class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==1 or nums[0]!=nums[1]:
            return nums[0] 
        for i in range(1,len(nums)-1):
            if nums[i-1]!=nums[i] and nums[i]!=nums[i+1]:
                return nums[i]
        return nums[-1]