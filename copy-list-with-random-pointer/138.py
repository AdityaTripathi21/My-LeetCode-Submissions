# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None): # type: ignore
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head

        mapping = {}

        # first pass
        while curr:
            new = Node(x = curr.val)
            mapping[curr] = new
            curr = curr.next

        # make sure to reset curr
        curr = head

        # 2nd pass
        while curr:
            new = mapping[curr]
            if curr.next:
                new.next = mapping[curr.next]
            else:
                new.next = None
            if curr.random:
                new.random = mapping[curr.random]
            else:
                new.random = None
            curr = curr.next
        
        return mapping[head]