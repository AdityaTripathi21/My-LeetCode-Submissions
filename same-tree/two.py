"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
res = true

root must be equal, if not return False 
recursively check left and right subtree

The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4

since the number of nodes can be 0, that means a tree being empty is valid, so if both are null, return True"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # type: ignore
        if p is None and q is None:
            return True

        """if p is None and q is not None:
            return False
        
        if p is not None and q is None:
            return False"""

        if p is None or q is None:  # easier check 
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
        
