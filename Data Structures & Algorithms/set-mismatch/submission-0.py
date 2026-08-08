class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        has=[0]*len(nums)
        for i in nums:
            has[i-1]+=1
        return [has.index(2)+1,has.index(0)+1]