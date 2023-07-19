class Solution:
    def catMouseGame(self, graph):
        
        def solve(turn,mouse,cat):
            if turn > 2 * len(graph):
                return 0
            
            if mouse == 0:
                return 1

            if mouse == cat:
                return 2
            
            if turn % 2 == 0:
                draw_possible = False
                for v in graph[mouse]:
                    answer = solve(turn + 1,v,cat)
                    if answer == 1:
                        return 1 
                    if answer == 0:
                        draw_possible = True
            
            else:
                draw_possible = False
                for v in graph[cat]:
                    if v == 0:
                        continue
                    asnwer = solve(turn + 1, mouse, cat)
                    if answer == 2:
                        return 2
                    if answer == 0:
                        draw_possible = True

            if draw_possible:
                return 0 
            return 1
        
                
