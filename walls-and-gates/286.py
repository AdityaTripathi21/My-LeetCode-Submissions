from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j))

        def is_valid(r, c):
            return 0 <= r < len(rooms) and 0 <= c < len(rooms[0]) and rooms[r][c] == 2147483647

        while q:
            x, y = q.popleft()
            if is_valid(x - 1, y):
                rooms[x - 1][y] = rooms[x][y] + 1
                q.append((x - 1, y))

            if is_valid(x + 1, y):
                rooms[x + 1][y] = rooms[x][y] + 1
                q.append((x + 1, y))

            if is_valid(x, y + 1):
                rooms[x][y + 1] = rooms[x][y] + 1
                q.append((x, y + 1))

            if is_valid(x, y - 1):
                rooms[x][y - 1] = rooms[x][y] + 1
                q.append((x, y - 1))