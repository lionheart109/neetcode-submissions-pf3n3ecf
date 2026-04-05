class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        c=0
        if nums:
            for i in range(len(nums)):
                s.add(nums[i])
            m = 1
            l = 1
            for si in nums:
                if si-1 in s:
                    continue
                st = si
                while st+1 in nums:
                    l+=1
                    st+=1
                m = max(m,l)
                l=1
            return m 
        return 0    