class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        has={}
        while i<len(nums):
            if nums[i] not in has:
                has[nums[i]]=1
                i+=1

            elif has[nums[i]]<2:
                has[nums[i]]+=1
                i+=1
            else:
                nums.pop(i)
        return len(nums)