"""Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

probably can be more than one valid path, only need one tho to return true
if no paths found, return false

go down left subtree and also go down right subtree

if we reached an empty node or the root is empty, return False

instead of using helper function, track state by just subtracting the node value from target
if the target is 0 and we're at a leaf node, return True



"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool: # type: ignore
        if root is None:
            return False

        cur = root.val
        targetSum -= cur

        if root.left is None and root.right is None and targetSum == 0:
            return True
        

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)