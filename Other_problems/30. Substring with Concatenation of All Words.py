class Solution:
    def findSubstring(self, s, words):
        substing_len = len(words) * len(words[0])
        if substing_len > len(s):
            return []
        
        def check_substring(substring, words):
            if len(substring) < substing_len:
                return False
            
            for word in words:
                if word in substring:
                    substring = substring.replace(word, "", 1)
            if substring == "":
                return True
            else:
                return False
        result = []
        increment = len(words[0])
        
        for i in range(len(s)):
            flag = False
            if len(s) - i  < substing_len:
                break
            if check_substring(s[i:i+substing_len], words):
                flag = True
                result.append(i)
            if flag:
                i += increment
            else:
                i += 1
        return result



sol = Solution()
s = "ababaab"
words = ["ab","ba","ba"]
print(sol.findSubstring(s, words))

