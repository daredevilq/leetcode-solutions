class Solution:
    def reverseWords(self, s) -> str:
        #triming  

        words = []

        word_start = 0
        word_end = 0

        while word_end < len(s):
            if s[word_end] == " ":
                if word_end != word_start:
                    words.append(s[word_start:word_end])
                    word_start = word_end + 1
                    word_end += 1
                else:
                    word_end += 1
                    word_start += 1
            else:
                word_end += 1
        
        if word_end != word_start:
            words.append(s[word_start:word_end])

        result = ""

        for i in range(len(words) - 1, 0, -1):
            result += words[i] + " "
        
        result +=  words[0]
        
        return result


s = "a good   example"

sol = Solution()
print(sol.reverseWords(s))