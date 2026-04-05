class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1
        print(int((len(s)-1)/2))
        while i < len(s)-1:
            if not s[i].isalnum():
                i += 1 
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower()==s[j].lower():
                if i == j:
                    print('in')
                    return True
                i += 1
                j -= 1
                continue
            return False
        return True