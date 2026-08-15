"""You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.

to keep track of exits, loop over maze and add exits to set
O(n) SC

is there a way to get better SC? Just check if a cell is an exit O(1) SC
need to use BFS because we need to find shortest path to exit

once you reach an exit, you don't need to take an extra step, so if you're at exit just return
keep track of number of steps -> don't need to

you would keep track of steps with dfs but with bfs, if you find an exit, that IS the shortest path

exits aren't guaranteed, if not found, return -1

need queue for bfs
need to mark cells as visited so change them to walls O(1) SC
even if the entrace is on the border, make sure it's not counted as exit
so when you do exit check, make sure it's on the border, equal to '.', and its coordinates aren't the entrance

once you discover cell, immediately mark as visited and add to queue"""

from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:   # type: ignore
        q = deque()
        steps = 0

        start_r, start_c = entrance

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        q.append(entrance)
        maze[start_r][start_c] = "+"

        while q:
            level = len(q)

            for _ in range(level):
                r, c = q.popleft()

                if steps > 0 and (
                    r == 0 
                    or c == 0 
                    or r == len(maze) - 1 
                    or c == len(maze[0]) - 1
                ):
                    return steps
                
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if (
                        0 <= new_r < len(maze)
                        and 0 <= new_c < len(maze[0])
                        and maze[new_r][new_c] == "."
                    ):
                        maze[new_r][new_c] = "+"
                        q.append((new_r, new_c))
            steps += 1
        
        return -1