# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            head = list1
            other = list2
        else:
            head = list2
            other = list1

        curr = head

        while curr.next is not None and other is not None:
            if curr.next.val <= other.val:
                curr = curr.next
            else:
                temp = other.next
                other.next = curr.next
                curr.next = other
                other = temp
                curr = curr.next

        if other is not None:
            curr.next = other

        return head
        
        