# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = [] 
        while head:
            st.append(head.val)
            head = head.next
        print(st)
        i, j = 0, len(st) - 1 
        while i < j:
            if st[i] != st[j]:
                return False
            i += 1
            j -= 1
        return True