# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        l=0
        if not head:
            return None
        while temp:
            temp=temp.next
            l+=1
        if l==1:
            return None
        elif l==n:
            return head.next
        temp=head
        for i in range(l-n-1):
            temp=temp.next
        d=temp.next
        temp.next=temp.next.next
        del d

        return head