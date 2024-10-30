#we make two pointers. One of the pointers point at the previous node and the other points at the current node. Since we are starting from head we have one 
#pointer as the head and the other as None. we go through the list and store the next node in a temporary variable then we set the next of the current node
#to the previous node using the pointer and then we set the pointer, which points to the previous node, to the current node and set the current node to the
#value stored in the temporary variable.
# None -> 1 -> 2 -> 3 -> 4 -> 5 -> None
# None -> 5 -> 4 -> 3 -> 2 -> 1 -> none

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev