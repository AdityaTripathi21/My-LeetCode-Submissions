# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(curr, low, high):
            if not curr:
                return True

            if curr.val > low and curr.val < high:
                return dfs(curr.left, low, curr.val) and dfs(curr.right, curr.val, high)
            else:
                return False


        return dfs(root, -inf, inf)