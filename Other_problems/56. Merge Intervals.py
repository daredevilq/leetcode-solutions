class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x: x[0])

        result = []
        
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if end >= interval[0]:
                end = max(end, interval[1])
            else:
                result.append([start, end])
                start, end = interval

        result.append([start, end])


        return result



sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
#intervals = [[1,4],[4,5]]
print(sol.merge(intervals))