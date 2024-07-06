class Solution:
    def largestPalindrome(self, n: int) -> int:
        upper_limit = 10**n - 1
        lower_limit = 10**(n-1)

        max_palindrome = 0 

        for i in range(upper_limit, lower_limit, -1):
            if i * i <= max_palindrome:
                break
            for j in range(i, lower_limit, -1): 
                product = i * j
                print(product)
                if product <= max_palindrome:
                    break 
                mult = str(product)
                if mult == mult[::-1]: 
                    max_palindrome = product

        return max_palindrome % 1337  

# Example usage:
sol = Solution()
print(sol.largestPalindrome(2)) 





