class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        i = 0
        j = 0
        set = {}

        for i in range(len(t)):
            set[t[i]] = False

        while i < len(s):
            pass