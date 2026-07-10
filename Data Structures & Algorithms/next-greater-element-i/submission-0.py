class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        has={}
        st=[]

        for i in range(len(nums2)-1,-1,-1):
            while st and st[-1]<=nums2[i]:
                st.pop()
            if st:
                has[nums2[i]]=st[-1]
            st.append(nums2[i])
        for i in range(len(nums1)):
            if nums1[i] in has:
                ans[i]=has[nums1[i]]

        return ans
            