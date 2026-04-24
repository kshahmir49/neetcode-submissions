class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            count = [0] * 26
            for k in s:
                count[ord(k)-ord("a")] += 1
            if tuple(count) not in d:
                d[tuple(count)] = [s]
            else:
                d[tuple(count)].append(s)
        return list(d.values())
        