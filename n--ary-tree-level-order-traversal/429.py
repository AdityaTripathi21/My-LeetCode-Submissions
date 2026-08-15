"""Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

need bfs for this to traverse level by level from left to right
res is a list of lists of int 
each level's res is a list of ints

bfs needs queue

simplest example:
1, 2, 3

if you have the root, add it to the queue, pop it
add children to queue

you need to remember the length of a level to add nodes, because otherwise
you don't know how many nodes are at a level because you add children which changes the len of the queue

forgot edge case if root is empty

SC: auxilary space is O(w) where w is the width of a level
technically it can hold more because you can have a queue with all nodes of a level, and then you pop one, and add its children

SC: O(n) because the res holds every single node
TC: O(n) because you visit every single node




"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]: # type: ignore
        if root is None:
            return []

        res = []
        q = deque()

        q.append(root)

        while q:
            level = []
            len_level = len(q)

            for _ in range(len_level):
                node = q.popleft()
                level.append(node.val)

                for child in node.children:
                        q.append(child)

            res.append(level)
        
        return res
            

            
