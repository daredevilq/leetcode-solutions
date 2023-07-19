class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1
        
        
        
        best_i = 0
        best_j = 0
        best_len = 1

        start = 1
        end = len(s)
        for i in range(len(s)):
            i = 0
            for j in range(start, end):
                if j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                        best_len = 2
                        best_j = j
                        best_i = i
                else:
                    if dp[i+1][j-1] == 1 and s[i] == s[j]:
                        dp[i][j] = 1
                        if  best_len< j - i + 1:
                            best_len = j - i + 1
                            best_i= i
                            best_j = j

                i +=1
            start +=1
        return s[best_i:best_j+1]
        
                


sol = Solution()
print(sol.longestPalindrome("cbbd"))
