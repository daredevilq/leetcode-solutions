
class Solution:
    def groupAnagrams(self, strs):
        hash_map = {}

        for i in range(len(strs)):
            sorted_string = ''.join(sorted(strs[i]))
            response = hash_map.get(sorted_string)
            if response != None:
                hash_map[sorted_string].append(strs[i])
            else:
                hash_map[sorted_string] = [strs[i]]

        result = []

        for key in hash_map:
            result.append(hash_map[key])

        return result


sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))
