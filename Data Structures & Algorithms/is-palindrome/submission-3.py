class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ""
        # removing punctuation
        for i in s:
            if (ord(i)>=ord("A") and ord(i)<=ord("z")) or (ord(i)>=ord("0") and ord(i)<=ord("9")):
                k += i
        print(k)
        k = k.lower()
        return k == k[::-1]