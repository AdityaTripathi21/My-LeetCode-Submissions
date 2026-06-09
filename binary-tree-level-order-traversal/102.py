# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            len_q = len(q)
            level = []
            for i in range(len_q):
                x = q.popleft()
                if x:
                    level.append(x.val)
                    q.append(x.left)
                    q.append(x.right)
            if level:
                res.append(level)
        return res