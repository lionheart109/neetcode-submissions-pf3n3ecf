from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       l1 = defaultdict(list)
       freq = defaultdict(int)
       alp = Counter('abcdefghikjlmnopqrstuvwxyz')
       for s in strs:
            alp.update(s)
            key = tuple(alp.items())
            l1[key].append(s)
            alp = Counter('abcdefghikjlmnopqrstuvwxyz')
       return list(l1.values())