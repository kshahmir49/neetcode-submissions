class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        tab = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    tab[i][j] = 1 + tab[i-1][j-1]
                else:
                    tab[i][j] = max(tab[i-1][j],tab[i][j-1])
        return tab[m][n]