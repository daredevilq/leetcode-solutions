class Solution:
    def numDistinct(self, s, t):
        
        def solve_incorrect(s,t,memo):
            ls = len(s)
            lt = len(t)

            if lt>ls:
                return 0
            
            if lt == 0:
                return 1
            
            if ls == 0 and lt != 0:
                return 0
            
            if (s,t) in memo:
                return memo[(s,t)]

            result1 = 0
            result2 = 0
            result = 0
            for i in range(1,len(s)+1):
                prefix_s = s[:i]
                prefix_t = t[:len(prefix_s)]
                #print(prefix_s, "preifx s")
                #print(prefix_t, "preifx t")
                #print()
                
                print(s, "s")
                print(t, "t")
                print()
                if prefix_s == prefix_t:
                    new_s = s.removeprefix(prefix_s)
                    new_t = t.removeprefix(prefix_t)
                    result1 +=  solve_incorrect(new_s, new_t, memo)

                new_s = s.removeprefix(prefix_s)
                result2 += solve_incorrect(new_s,t,memo)

                result = result1 + result2
            memo[(s,t)] =result
            return result
        
        memo = {}
        ans = solve_incorrect(s, t, memo)     # nieprawilowy solve
       

        def solve(i, j, memo):
            if j < 0:
                return 1

            if i < 0:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:
                memo[(i, j)] = solve(i - 1, j - 1, memo) + solve(i - 1, j, memo)
            else:
                memo[(i, j)] = solve(i - 1, j, memo)

            return memo[(i, j)]

        memo = {}
        ans = solve(len(s) - 1, len(t) - 1, memo)     
        return ans


word = "piotrsmialek"

sol = Solution()
s = "rabbbit" 
t = "rabbit"
s = "babgbag"
t = "bag"
print(sol.numDistinct(s,t))

