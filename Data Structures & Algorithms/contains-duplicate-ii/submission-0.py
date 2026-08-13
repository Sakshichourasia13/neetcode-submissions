class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        has={}
        for i in range(len(nums)):
            if nums[i] in has:
                v=has[nums[i]]
                if i-v<=k and i-v>0:
                    return True
                has[nums[i]]=abs(v-i)
            else:
                has[nums[i]]=i
        return False