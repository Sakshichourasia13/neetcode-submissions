class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has=[]
        for i in nums:
            if i in has:
                return True
            has.append(i)
        return False