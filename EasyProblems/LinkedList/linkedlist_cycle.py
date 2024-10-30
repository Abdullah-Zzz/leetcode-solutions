#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. we create a hashmap 
#to store the nodes. we go through the list and store the current node and check if the next node is in the hashmap. If it is that means that the linked list has
#a cycle and if it is not we go to the next node and repeat the process.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = set()
        curr = head
        while curr:
            hashmap.add(curr)
            if curr.next in hashmap:
                return True
                break
            else:
                curr = curr.next
        return False