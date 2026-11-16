class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        has={i[0]:i[1] for i in nums1}

        for i in nums2:
            if i[0] in has:
                has[i[0]]+=i[1]

            else:
                has[i[0]]=i[1]
        
        ans=[[i,has[i]] for i in has]
        return sorted(ans,key=lambda x:x[0])


