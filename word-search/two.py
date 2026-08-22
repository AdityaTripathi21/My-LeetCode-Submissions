"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

m == board.length
n = board[i].length
1 <= m, n <= 6 
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


can't move diagonal, only move up, down, left, right
tiny input size -> large TC

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

If I'm exploring cells, I need a way to mark them as visited so I don't explore them again
ex: let's say I go down from a cell, from the next cell, I can still go up and return to that previous cell,
however this is disallowed, so I need a way to not go to that cell, so maintain a set of visited cells
however this set is not permanent, and only for the current path, if my current path doesn't work out,
another path can still use that cell, so each path should maintain its own visited set, so the set must be passed as an argument for recursion

I can return if my current path is equal to the word
if you explore a cell, and it is valid (within bounds, not yet visited), only THEN you check if it matches the current letter in the word, if it does, recurse from it, otherwise, backtrack

choices: Choose any 4 adjacent cells based on constraints
constraints: cell must be within bounds and not currently visited on the path
base case: path is equal to word
backtrack: if current cell isn't equal to the current letter in the word, backtrack and try other cells

must do the algorithm from every single cell in the grid
don't need a path because the problem isn't asking for one, it's asking for T/F
you use the position instead, because if you're on pos 3, that means you already matched the past 3 letters correctly

so the state is (row, col), visited set, and position

note: I need to think more about the recursive calls themselves
when the helper function returns True, I need to propogate that result upwards
if a helper call returns True, that means the word is found, so I can return True from there as well
otherwise, in all scenarios, return False
"""



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:     # type: ignore
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def helper(r, c, pos):
            if pos == len(word):
                return True
            
            if (
                r < 0
                or r >= len(board)
                or c < 0
                or c >= len(board[0])
                or (r, c) in visited
                or board[r][c] != word[pos]
            ):
                return False
            else:   # valid cell
                visited.add((r,c))
                for dr, dc in directions:
                    if helper(r+dr, c + dc, pos + 1):
                        visited.remove((r,c))   # not necessary
                        return True
                visited.remove((r,c))   # this means that all 4 neighbors failed, this current path doesn't lead to anywhere
                return False
                
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if helper(r, c, 0):
                    return True
        
        return False
                    
                    

                
            