class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        res = False

        def dfs(i, visited, row, col):
            nonlocal res

            if i == len(word):
                res = True
                return 
            
            if row == len(board) or row < 0:
                return 
            
            if col == len(board[0]) or col < 0:
                return
            
            if (row, col) in visited:
                return
            
            if board[row][col] == word[i]:
                visited.add((row, col))
                dfs(i + 1, visited, row, col + 1)
                dfs(i + 1, visited, row, col - 1)
                dfs(i + 1, visited, row + 1, col)
                dfs(i + 1, visited, row - 1, col)
                visited.remove((row, col))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(0, set(), i, j)
        
        return res