class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        lf=[]
        l=[[]for n in range(len(nums)+1) ]
        for n in nums:
            freq[n] += 1
        for kv,v in freq.items():
            l[v].append(kv)
        i=len(l)+1
        for i in l[::-1]:
            if i and k>0:
              c=0
              for j in i:
                lf.append(j)
                k-=1
        return lf