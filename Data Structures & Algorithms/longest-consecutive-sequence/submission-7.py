class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        if nums:
            for i in nums:
                s.add(i)
            m = 1
            l = 1
            for si in nums:
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