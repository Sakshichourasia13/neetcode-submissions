# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        n2=0
        while l1:
            n1=n1*10+l1.val
            l1=l1.next
        while l2:
            n2=n2*10+l2.val
            l2=l2.next

        n1+=n2
        head=None
        for i in str(n1):
            if not head:
                head=ListNode(int(i))
                temp=head
            else:
                temp.next=ListNode(int(i))
                temp=temp.next
        return head
