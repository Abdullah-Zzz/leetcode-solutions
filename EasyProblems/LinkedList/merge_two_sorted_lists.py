#we make a dummy list in which we will store the nodes one by one after checking which node's value is greater. we go through list1 and list2 and check each 
#node's value if the value of node from list1 is greater than the value of the node from list2 then we set list2 to the next node and store the smaller node 
#in the dummy list. we do this until we reach the end of the list.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val :
                curr.next=list1
                list1 =list1.next
            else:
                curr.next=list2
                list2 =list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next=list2
        return dummy.next