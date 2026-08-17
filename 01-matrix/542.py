"""Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

mat isn't empty
find nearest 0 -> need bfs 
if a cell is 0, just return 0

if a cell is 1, check its 4 neighbors
maybe we could just use dp

dp mat is initalized as 0s
if you find a 0, just keep it as 0
if you find a 1, take the min of the dp of its neighbors and just add 1

don't need bfs I think can just use dp
nvm don't use dp because some values haven't been computed yet

use bfs 
put every 0 into the queue
give every 1 an infinite distance

do bfs from all 0s simultaneously
multi source bfs -> just do bfs from multiple sources

loop through mat, if a cell is 0, set distance to 0, enqueue that cell
if 1, set distance to inf 

go through q, pop node, if neighbor distance is inf -> means univisited, set distance to node distance + 1
add neighbor to q

return mat
note: even though creating separate distance mat is clearer, uses extra space, just modify mat in place"""

from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]: # type: ignore
        q = deque()
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    mat[r][c] = float("inf")
                else:
                    q.append((r, c))
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                if r + dr >= 0 and r + dr < len(mat) and c + dc >= 0 and c + dc < len(mat[0]) and mat[r+dr][c+dc] == float("inf"):
                    mat[r+dr][c+dc] = 1 + mat[r][c]
                    q.append((r+dr, c + dc))
                
        
        return mat
