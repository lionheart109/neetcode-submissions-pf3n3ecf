from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       l1 = defaultdict(list)
       for s in strs:
            key = tuple(sorted(s))
            l1[key].append(s)
       return list(l1.values())