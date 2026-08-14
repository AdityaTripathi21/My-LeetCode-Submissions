"""Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

basically switch left and right sides

what happens if left is none or right is none 
still swap? yeah I think so 

The number of nodes in the tree is in the range [0, 100].   ->  tree can be empty
-100 <= Node.val <= 100 -> doesn't really matter"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # type: ignore
        if root is None:
            return None

        left = root.left
        right = root.right

        root.left = right
        root.right = left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        
