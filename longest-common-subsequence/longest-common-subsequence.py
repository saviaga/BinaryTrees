class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        N, M = len(text1), len(text2)
        DP = [[0 for i in range(M+1)] for j in range(N+1)]
        for i in range(N):
            for j in range(M):
                if(text1[i]==text2[j]):
                    DP[i+1][j+1]=DP[i][j]+1
                else:
                    DP[i+1][j+1] = max(DP[i][j+1],DP[i+1][j])
        return (DP[-1][-1])            
          


        

        