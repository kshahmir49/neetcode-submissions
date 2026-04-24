class Solution:
    def isPalindrome(self, s: str) -> bool:
        # k = ""
        # # removing punctuation
        # for i in s:
        #     if (ord(i)>=ord("A") and ord(i)<=ord("z")) or (ord(i)>=ord("0") and ord(i)<=ord("9")):
        #         k += i
        # k = k.lower()
        # return k == k[::-1]
        i = 0
        k = len(s)-1
        while i<=k:
            while not s[i].isalnum() and i<k: i+=1
            while not s[k].isalnum() and k>i: k-=1
            if s[i].lower()!=s[k].lower(): return False
            i+=1
            k-=1
        return True