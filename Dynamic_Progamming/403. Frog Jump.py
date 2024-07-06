class Solution:
    
    def dynamic(self, curr_position, prev_position, stones, memo):
        if curr_position == len(stones) - 1:
            return True
        
        if (curr_position, prev_position) in memo:
            return memo[(curr_position, prev_position)]
        
        
        k_jump = False
        k_plus_one = False
        k_minus_one = False

        for next_position in range(curr_position + 1, len(stones)):
            if stones[next_position] == stones[curr_position] - stones[prev_position]:
                k_jump = self.dynamic(next_position, curr_position, stones, memo)
            if stones[next_position] == stones[curr_position] - stones[prev_position] + 1:
                k_plus_one = self.dynamic(next_position, curr_position, stones, memo)
            if stones[next_position] == stones[curr_position] - stones[prev_position] - 1:
                k_minus_one = self.dynamic(next_position, curr_position, stones, memo)
            memo[(curr_position, next_position)] = k_jump or k_plus_one or k_minus_one

        return memo[(0, len(stones) -1)]

            
    
    def canCross(self, stones):
        memo = {}

        memo[(0,1)] = True

        result = self.dynamic(1,0,stones, memo)
        return result
    



class Solution:
    
    def dynamic(self, curr_position, last_jump, stones, stone_positions, memo):
        if curr_position == len(stones) - 1:
            return True
        
        if (curr_position, last_jump) in memo:
            return memo[(curr_position, last_jump)]
        
        for jump in [last_jump - 1, last_jump, last_jump + 1]:
            if jump > 0:
                next_position = stones[curr_position] + jump
                if next_position in stone_positions:
                    next_index = stone_positions[next_position]
                    if self.dynamic(next_index, jump, stones, stone_positions, memo):
                        memo[(curr_position, last_jump)] = True
                        return True
        
        memo[(curr_position, last_jump)] = False
        return False
    
    def canCross(self, stones):
        if not stones:
            return False
        
        stone_positions = {stone: i for i, stone in enumerate(stones)}
        print(stone_positions)
        memo = {}
        return self.dynamic(0, 0, stones, stone_positions, memo)

# Example usage:
sol = Solution()
print(sol.canCross([0,1,3,5,6,8,12,17]))  # Output: True
print(sol.canCross([0,1,2,3,4,8,9,11]))   # Output: False
