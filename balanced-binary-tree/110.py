# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: # type: ignore
        if not root:
            return True

        self.balanced = True

        def dfs(curr):
            if not curr:
                return 0

            l = dfs(curr.left)
            r = dfs(curr.right)

            if not(l - r >= -1 and l - r <= 1):
                self.balanced = False

            return max(l, r) + 1
        
        dfs(root)
        return self.balanced