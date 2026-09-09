# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        k=k%len(arr)
        arr[::]=arr[-k:]+arr[:-k]

        temp=head
        for i in arr:
            temp.val=i
            temp=temp.next
        return head