class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0

        def bct(i,sbs):
            nonlocal ans
            x=0
            for t in sbs:
                x^=t
            ans+=x

            for j in range(i,len(nums)):
                sbs.append(nums[j])
                bct(j+1,sbs)
                sbs.pop()
            
        bct(0,[])
        return ans