# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head
        size = 1
        node = head
        while (node.next != None):
            node = node.next
            size += 1

        index = size - n
        if (index < 0):
            return head
        if (index == 0):
            head = head.next
            return head
        
        node = head
        for i in range(index - 1):
            node = node.next
        
        temp = node.next.next
        node.next.next = None
        node.next = temp
        return head
        