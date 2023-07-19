from queue import Queue

class Node:
    def __init__(self, val = 0, neighbors=None ):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    def cloneGraph(self, node):
        visited = []
        queue = Queue()
        max_val = -1
        queue.put(node)
        while not queue.empty():
            v = queue.get()
            max_val = max(max_val, v.val)
            for u in v.neighbors:
                if u not in visited:
                    queue.put(u)
            
            visited.append(v)

        #to DO





        