class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lt = len(t)
        ls = len(s)

        if (lt != ls):
            return False
        
        dt = {}
        ds = {}

        for i in range(lt):
            if (s[i] in ds):
                ds[s[i]] = ds[s[i]] + 1
            else:
                ds[s[i]] = 1
            if (t[i] in dt):
                dt[t[i]] = dt[t[i]] + 1
            else:
                dt[t[i]] = 1
        return dt == ds

        