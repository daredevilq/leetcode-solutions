class Solution:
    def minWindow(self, s, t) -> str:
        left = 0
        right = 0
        
        actual_leng = 0
        min_leng = 0
        set = {}
        
        for i in range(len(t)):
            set[t[i]] = False


        while left < len(s):
            pass