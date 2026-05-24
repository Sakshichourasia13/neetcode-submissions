class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        for i in range(len(nums)):
            d=target-nums[i]
            if nums[i] in has:
                return [has[nums[i]],i]
            has[d]=i
            # print(has)
        