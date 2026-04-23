# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 
        curr = head 
        length = 0 
        while curr:
            length += 1
            curr = curr.next 
        
        if length == 0:
            return head
        
        k = k % length 
        if k == 0:
            return head 
        
        n = length - k - 1
        count = 0
        curr = head
        while count < n:
            curr = curr.next 
            count += 1

        nhead = curr.next
        curr.next = None

        tail = nhead
        while tail.next:
            tail = tail.next 
        tail.next = head
        
        return nhead