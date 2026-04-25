class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = []
        l,r = 0,0
        res = 0
        while r<len(s):
            while s[r] in st:
                st.remove(s[l])
                l+=1
            st.append(s[r])
            res = max(res,r-l+1)
            r+=1
        return res
