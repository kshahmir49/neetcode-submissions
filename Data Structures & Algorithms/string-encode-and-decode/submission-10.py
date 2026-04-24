class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(i))+"#"+i for i in strs])

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            l.append(s[j+1:j+1+int(s[i:j])])
            i = j+1+int(s[i:j])
        return l