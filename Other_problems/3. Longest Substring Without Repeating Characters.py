class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        SIZE = 128
        array = [False] * SIZE
        i = 0
        max_len = 0
        acc_len = 0
        end = i

        while i < len(s):
            if array[ord(s[i])]:
                acc_len = 1
                array = [False] * SIZE
            else:
                acc_len +=1
                array[ord(s[i])] = True
                max_len = max(max_len, acc_len)
            i +=1

        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        dict = {}
        max_len = 0
        start = 0
        for i in range(len(s)):
            last_index = dict.get(s[i]) 
            if last_index != None and last_index >=start:
                start = last_index + 1
            
            max_len = max(max_len, i - start+ 1)
            
            dict[s[i]] = i

        return max_len






sol = Solution()
s ="bbbbb"
s ="abba"
#s ="abcabcbb"
#s ="bbbbb"
#s ="pwwkew"
print(sol.lengthOfLongestSubstring(s))

