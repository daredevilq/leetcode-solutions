class Solution:
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0

        # Initialize the result array with 1 candy for each child
        result = [1] * n

        # Traverse from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1

        # Traverse from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                result[i] = max(result[i], result[i + 1] + 1)

        return sum(result)

# Example usage
ratings = [1, 0, 2]
sol = Solution()
print(sol.candy(ratings))  # Output: 5

ratings = [1, 2, 2]
print(sol.candy(ratings))  # Output: 4
