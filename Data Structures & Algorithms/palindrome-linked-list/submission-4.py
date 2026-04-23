# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head 
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
        prev = None
        curr = slow.next
        while curr:
            next_curr = curr.next 
            curr.next = prev
            prev = curr 
            curr = next_curr
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next 
            prev = prev.next 
        return True
