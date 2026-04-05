class Solution:

    def encode(self, strs: List[str]) -> str:
        e=''
        for s in strs:
            e=e+str(len(s))+'#'+s
        print(e)
        return e
    def decode(self, s: str) -> List[str]:
        ans = []
        i=0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            print(s[i:j])
            length = int(s[i:j])
            i = j + 1
            print(f'length = {length}')
            word = s[i:i+length]
            print(word)
            ans.append(word)
            i += length
        print(ans)
        return ans
                

