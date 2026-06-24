# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone_map = {}  # original -> cloned
        clone_map[node] = Node(node.val, [])
        q = deque([node])

        while q:
            current = q.popleft()

            for neighbor in current.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)  # only append neighbors to queue if they haven't been seen
                clone_map[current].neighbors.append(clone_map[neighbor])    # add clone connection

        return clone_map[node]