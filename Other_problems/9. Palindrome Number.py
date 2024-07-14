class Solution:
    def isPalindrome(self, x):
        x_copy = str(x)[::-1]

        return x_copy == str(x)



sol = Solution()
sol.isPalindrome(-102)