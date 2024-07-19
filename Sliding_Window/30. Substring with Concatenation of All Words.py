class Solution:
    def findSubstring(self, s, words):
        word_len = len(words[0])
        words_number = len(words)
        actual_matching = 0
        result_arr = []
        hash_map = {}
        hash_map_template = {}

        for i in range(len(words)):
            result = hash_map.get(words[i])
            if result:
                hash_map[words[i]] = result + 1 
                hash_map_template[words[i]] = result + 1 
            
            else:
                hash_map[words[i]] = 1
                hash_map_template[words[i]] =  1 
        
        
        i = 0
        j = 0

        while i < len(s):
            if i + word_len <= len(s):
                word = s[i: i + word_len]
                result = hash_map.get(word)
                if result and result > 0:
                    actual_matching += 1
                    hash_map[word]= result - 1
                    i += word_len
                    if actual_matching == len(words):
                        result_arr.append(j)
                        actual_matching = 0
                        while j < i:
                            word = s[j : j + word_len]
                            occurs = hash_map.get(word) 
                            if occurs != None and occurs < hash_map_template.get(word):
                                hash_map[word] += 1
                            j+=word_len
    
                else:
                    actual_matching = 0
                    i += word_len
                    while j < i:
                        word = s[j : j + word_len]
                        occurs = hash_map.get(word) 
                        if occurs != None and occurs < hash_map_template.get(word):
                            hash_map[word] += 1
                        j+=word_len
        
        return result_arr


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cnt = Counter(words)
        m, n = len(s), len(words)
        k = len(words[0])
        ans = []
        for i in range(k):
            cnt1 = Counter()
            l = r = i
            t = 0
            while r + k <= m:
                w = s[r : r + k]
                r += k
                if w not in cnt:
                    l = r
                    cnt1.clear()
                    t = 0
                    continue
                cnt1[w] += 1
                t += 1
                while cnt1[w] > cnt[w]:
                    remove = s[l : l + k]
                    l += k
                    cnt1[remove] -= 1
                    t -= 1
                if t == n:
                    ans.append(l)
        return ans

sol = Solution()
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(sol.findSubstring(s, words))

