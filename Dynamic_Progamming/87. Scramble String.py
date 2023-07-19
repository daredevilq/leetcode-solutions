class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def recursive(string1, string2):
            if len(string1) == 1 and len(string2) == 1:
                return string1 == string2
            
            res1= False
            res2 = False
            for i in range(1,len(string1)):
                x = string1[i:]
                y = string1[:i]

                res1 = recursive()




sol = Solution()
s1 = "abcde"
s2 = "caebd"
print(sol.isScramble(s1,s2))