from queue import Queue
from queue import PriorityQueue
from math import inf

#There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

#Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

#The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.



def relaxation(maze, y, x, ny, nx, distance, path, dd):
    if distance[ny][nx] >= distance[y][x] + 1:
        distance[ny][nx] = distance[y][x] + 1
        word = path[y][x]
        if word == "":
            path[ny][nx] = dd
            return True
        
        if word[-1] == dd:
            path[ny][nx] = max(path[y][x], path[ny][nx])
        else:
            path[ny][nx] = max(path[y][x] + dd, path[ny][nx])
        return True
    return False

def maze_dijkstra(maze, start, end):
    queue = PriorityQueue()
    queue.put((0, start[0], start[1]))
    visited = [[False]*len(maze[0]) for _ in range(len(maze))]
    distance = [[inf]*len(maze[0]) for _ in range(len(maze))]
    path = [[""]*len(maze[0]) for _ in range(len(maze))]
    distance[start[0]][start[1]] = 0
    
    while not queue.empty():
        dist, y, x = queue.get()
        for dy, dx, dd in [(-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]:
            nx, ny = x, y
            nx += dx
            ny += dy
            if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] == 0:
                if visited[ny][nx] == False:
                    if relaxation(maze, y, x, ny, nx, distance, path, dd):
                        queue.put((distance[ny][nx], ny, nx))

        visited[y][x] = True

    for i in path:
        print(i)
    
    for i in distance:
        print(i)

    if distance[end[0]][end[1]] == inf:
        return "impossible"
    return path[end[0]][end[1]]

maze = [[0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0]]




print(maze_dijkstra(maze, (4, 3), (0, 1)))