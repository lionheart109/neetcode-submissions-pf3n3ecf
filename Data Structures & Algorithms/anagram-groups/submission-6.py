class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     l1 = defaultdict(list)
     alp = [0]*26
     print(alp)
     for s in strs:
        alp = [0]*26
        for c in s:
            alp[ord(c)-97] += 1
        l1[tuple(alp)].append(s)
     return list(l1.values())