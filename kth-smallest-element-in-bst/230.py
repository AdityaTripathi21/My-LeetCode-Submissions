# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(curr, count):
            if not curr:
                return
            
            dfs(curr.left, count)
            if count == k:
                return curr.val
            dfs(curr.right, count + 1)
        
        return dfs(root, 1) # type: ignore