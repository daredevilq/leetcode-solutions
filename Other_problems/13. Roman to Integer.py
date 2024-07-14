class Solution:
    def romanToInt(self, s) -> int:
        set = {}

        set["I"] = 1
        set["V"] = 5
        set["X"] = 10
        set["L"] = 50
        set["C"] = 100
        set["D"] = 500
        set["M"] = 1000
        set["IV"] = 4
        set["IX"] = 9
        set["XL"] = 40
        set["XC"] = 90
        set["CD"] = 400
        set["CM"] = 900

        index = 0
        result = 0
        while index < len(s):
            if index + 1 < len(s):
                temp = set.get(s[index] + s[index + 1])
                if temp!= None:
                    result += temp
                    index += 2
                else:
                    result += set.get(s[index])
                    index +=1
            else:
                    result += set.get(s[index])
                    index+=1

        return result
    

s = "MCMXCIV"
sol = Solution()
print(sol.romanToInt(s))