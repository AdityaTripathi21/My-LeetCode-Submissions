# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: # type: ignore
        
        def isSameTree(p, q):
            if not q and not p:
                return True
            if not p and q:
                return False
            if p and not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        def has_subtree(p):
            if not p:
                return False
            if p.val == subRoot.val:
                res = isSameTree(p, subRoot)
                if res == False:
                    return has_subtree(p.left) or has_subtree(p.right)
                return res
            if p.val != subRoot.val:
                return has_subtree(p.left) or has_subtree(p.right)
        
        return has_subtree(root) # type: ignore