# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None):
            return False
        s = set()
        node = head

        while (node.next != None):
            node = node.next
            if (node in s):
                return True
                continue
            s.add(node)
        return False
        