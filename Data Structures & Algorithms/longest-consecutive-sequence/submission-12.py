class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            s = set(nums)
            m = 1
            l = 1
            for si in s:
                if si-1 in s:
                    continue
                st = si
                while st+1 in s:
                    l+=1
                    st+=1
                m = max(m,l)
                l=1
            return m 
        return 0    