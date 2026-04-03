class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in range(len(strs)):
            s += strs[i] + "漢"
        return s.strip()
        

    def decode(self, s: str) -> List[str]:
        strs = s.split("漢")
        strs.pop()
        return strs
