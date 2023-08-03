class Solution:
    def strongPasswordChecker(self, password):
        big_letter = False
        small_letter = False
        digit = False
        no_characters = len(password)
        
        repreating_strings = []
        no_repreats = 0
        if no_characters < 6:
            return 6 - no_characters
        
        if no_characters > 20:
            return no_characters - 20
        
        streak = 1
        for i in range(len(password)):
            if password[i].isupper():
                big_letter = True
            if password[i].islower():
                small_letter = True
            if password[i].isdigit():
                digit = True
            print(streak)
            if i > 0:
                if password[i] == password[i-1]:
                    streak += 1
                else:
                    if streak >= 3:
                        repreating_strings.append([i-streak, i-1, streak])
                        no_repreats += streak 
                    streak = 1
        if streak >= 3:
            repreating_strings.append([i-streak+1, i, streak])

        min_numbers_of_operations = 0

        if no_repreats == 0:
            if not big_letter:
                min_numbers_of_operations += 1
            if not small_letter:
                min_numbers_of_operations += 1
            if not digit:
                min_numbers_of_operations += 1
            return min_numbers_of_operations
        
        




sol = Solution()
print(sol.strongPasswordChecker("aaakkk11111"))
