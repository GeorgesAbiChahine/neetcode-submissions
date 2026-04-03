class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        if s == '' or s == ' ':
            return True
        i, j = 0, len(s) -1
        while i < j:
            if not (s[i].isalpha() or s[i].isnumeric()):
                i += 1
            elif not (s[j].isalpha() or s[j].isnumeric()):
                j -= 1
            else:
                if i == j:
                    break
                if s[i] != s[j]:
                    print(i,j)
                    return False
                else:
                    i +=1
                    j -=1
        return True
        