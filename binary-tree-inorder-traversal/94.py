"""Given the root of a binary tree, return the inorder traversal of its nodes' values.

inorder -> l root r
go into left subtree, go to root, go to right subtree"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        res = []

        def traverse(node):
            if node is None:
                return 
            
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)

        traverse(root)
        return res
