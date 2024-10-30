# we go through the list and determine the number of nodes in the list or the length of the list. we divide the len by 2 to get the middle index. Then we simply 
#go to that index and return the list with the middle node as the head. 



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        middle = head
        while curr:
            count+=1
            curr=curr.next
        count = count//2
        for i in range(count):
            middle = middle.next
        return middle