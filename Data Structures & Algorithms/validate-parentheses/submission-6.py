class Solution:
    def isValid(self, s: str) -> bool:

        if (s == ''):
            return True
        if (s == ' '):
            return True

        OPENERS = ['[', '{', '(']
        CLOSERS = [']', '}', ')']

        m = []
        for i in range(len(s)) :
            if (s[i] in OPENERS):
                m.append(s[i])
            else:
                if (len(m) == 0):
                    return False
                c = m.pop()
                st = c + s[i]
                if (st == '()' or st == '{}' or st == '[]'):
                    continue
                else:
                    return False
        
        return len(m) == 0
