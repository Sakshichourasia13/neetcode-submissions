# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp=head
        if not head:
            return None
        while temp and temp.next:
            if temp.next.val==val:
                a=temp.next
                temp.next=temp.next.next
                del a
            else:
                temp=temp.next
        if head.val==val:
            head=head.next
        return head