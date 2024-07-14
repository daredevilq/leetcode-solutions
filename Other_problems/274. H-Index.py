class Solution:
    def hIndex(self, citations) -> int:
        citations.sort()
        
        H_index = 0

        for i in range(len(citations) - 1, -1, -1):
            H_index = max(H_index, min(citations[i], len(citations) - i ))
    
        return H_index
    



sol = Solution()
citations = [3,0,6,1,5]

print(sol.hIndex(citations))
        