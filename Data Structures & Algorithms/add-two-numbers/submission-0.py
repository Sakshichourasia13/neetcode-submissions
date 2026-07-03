# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def num(self,head):
        s=""
        while head:
            s+=str(head.val)
            head=head.next

        return s[::-1]

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans=int(self.num(l1))+int(self.num(l2))

        ans=str(ans)[::-1]
        head=temp=ListNode(ans[0])
        for i in range(1, len(ans)):
            temp.next=ListNode(ans[i])
            temp=temp.next
        return head
            