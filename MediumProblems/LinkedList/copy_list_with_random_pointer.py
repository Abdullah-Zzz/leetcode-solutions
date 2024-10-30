#https://www.youtube.com/watch?v=DAzEniVtkMQ


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None

        curr = head
        old={} 

        while curr: 
            node = Node(x=curr.val)
            old[curr] =  node
            curr = curr.next

        curr = head
        while curr:
            newNode = old[curr]
            newNode.next = old[curr.next] if curr.next  else None
            newNode.random = old[curr.random] if curr.random else None
            curr = curr.next
        return old[head]
