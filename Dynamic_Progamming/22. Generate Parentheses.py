class Solution:
    def generateParenthesis(self, n: int):
        result = []
        def rec(left,right,string):
            
            if len(string) == 2*n:
                result.append(string)
            
            if left < n:
                rec(left + 1, right, string + '(')
            if right<left:
                rec(left , right + 1, string + ')')
        
        rec(0,0,'')
        return result










test = Solution()
print(test.generateParenthesis(3))