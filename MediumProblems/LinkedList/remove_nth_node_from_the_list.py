#to find the index from the start of the list we first find the length of the list and then we minus n from it. We get the index from the start of the list.
#if the index is 1 meaning it is the head of the list we simply set the head to the next node else we go to the node which comes before the index and set its
#next value to the next node's next.  


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 1
        while curr:
            count +=1
            curr = curr.next
        count = count-n
        if count==1:
            head = head.next
            return head
        else:
            removed = head
            for i in range(count):
                if i+2 == count:
                    removed.next = removed.next.next
                else:
                    removed = removed.next
            return head