from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # check if reshape is possible
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat

        # first create matrix of dim r x c
        matrix = [[0 for _ in range(c)] for _ in range(r)]


        # loop over all elements in old matrix
        # i is used to flatten matrix and we use 
        # modulo and division operator to map old coords to new
        for i in range(n*m):
            old_row = i // n
            old_col = i % n

            new_row = i // c
            new_col = i % c

            matrix[new_row][new_col] = mat[old_row][old_col]

        return matrix